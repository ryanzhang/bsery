from datetime import date, timedelta
import math
import pytest
from kupy.dbadaptor import DBAdaptor
from kupy.logger import logger
from bsery.big_small_eft_rotate import BigSmallEtfRotateStrategy
from bsery.stockutil import *
import os

given = pytest.mark.parametrize
skipif = pytest.mark.skipif
skip = pytest.mark.skip
xfail = pytest.mark.xfail


class TestStockUtil:
    @pytest.fixture(scope="class")
    def util(self):
        return StockUtil()

    def test_is_trade_day(self, util: StockUtil):
        assert util.is_trade_day(date(2022, 1, 27))
        assert util.is_trade_day(date(2022, 1, 28))
        assert not util.is_trade_day(date(2022, 1, 29))
        with pytest.raises(Exception) as exc_info:
            assert util.is_trade_day(date(1980, 1, 1))
        assert exc_info.value.args[0] == "没有找到给定日期的交易信息"
        assert str(exc_info.value) == "没有找到给定日期的交易信息"

    def test_get_trade_day_by_offset(self, util: StockUtil):
        assert util.get_trade_day_by_offset(date(2022, 1, 28), 1) == date(
            2022, 1, 27
        )
        assert util.get_trade_day_by_offset(date(2022, 1, 28), 2) == date(
            2022, 1, 26
        )
        assert util.get_trade_day_by_offset(date(2022, 1, 28), 5) == date(
            2022, 1, 21
        )
        assert util.get_trade_day_by_offset(date(2022, 1, 29), 1) == date(
            2022, 1, 27
        )

        assert util.get_trade_day_by_offset(date(2022, 1, 28), -1) == date(
            2022, 2, 7
        )
        assert util.get_trade_day_by_offset(date(2022, 1, 29), -1) == date(
            2022, 2, 8
        )
