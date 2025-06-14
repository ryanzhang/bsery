from datetime import date

from kupy.dbadaptor import DBAdaptor


class StockUtil:
    def __init__(self):
        db = DBAdaptor()
        self.trade_calendar = db.get_df_by_sql(
            "select * from stock.trade_calendar where exchange_cd='XSHG'"
        )

    def is_trade_day(self, start_date: date) -> bool:
        """判断给定日期是否可交易日期

        Args:
            start_date (date): 给定的日期

        Returns:
            bool: True 表示可交易，False 不可交易
        """
        df = self.trade_calendar
        ret = df.loc[df["calendar_date"] == start_date, "is_open"]
        if ret.shape[0] == 0:
            raise Exception("没有找到给定日期的交易信息")
        return ret.iloc[0]

    def get_trade_day_by_offset(self, trade_date: date, offset: int) -> date:
        """根据offset 推算给定日期之前或之后的诺干交易日
        如果offset == 0 就是算出 给定日之前的最近交易日，包括给定日期
        如果offset >0 就是推算给定日期最近的过去交易日往过去推offset个交易日
        如果offset <0 就是推算给定日期最近的将来交易日往过去推offset个交易日

        Args:
            trade_date (date): 给定的日期
            offset (int): 如果正数 则计算经过offset个交易日的可交易日期，如果负数则计算过去的交易日
            返回的交易日与给定的日期之间的可交易日期等于offset日期,注意不包含给定的那个日期

        Returns:
            date: [description]
        """
        # 如果给定日期不是交易日，就需要将offset 增1

        df = self.trade_calendar[self.trade_calendar["is_open"]]
        if offset >= 0:
            df = df.loc[
                df["calendar_date"] <= trade_date, "calendar_date"
            ].shift(offset)
            ret = df.iloc[-1]

        elif offset < 0:
            df = df.loc[
                df["calendar_date"] >= trade_date, "calendar_date"
            ].shift(offset)
            ret = df.iloc[0]

        return ret
