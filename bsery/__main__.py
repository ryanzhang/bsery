# -*- coding: UTF-8 -*-
import argparse
from datetime import date  # pragma: no cover

from kupy.logger import logger

from bsery.big_small_eft_rotate import BigSmallEtfRotateStrategy

# from . import BaseClass, base_function  # pragma: no cover


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m bsery` and `$ bsery `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(
        description="bsery big_small_etf_rotate strategy",
        epilog="Enjoy the bsery functionality!",
    )
    # # This is required positional argument
    # parser.add_argument(
    #     "name",
    #     type=str,
    #     help="The username",
    #     default="ryanzhang",
    # )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()
    # print(f"{args.message} {args.name}!")
    if args.verbose:
        print("Verbose mode is on.")
        # logging.basicConfig(
        #     level=logging.INFO, format=" %(asctime)s - %(levelname)s- %(message)s"
        # )

    logger.info("Executing main function")
    bsery = BigSmallEtfRotateStrategy(1)
    today = date.today()
    df = bsery.get_strategy_by_date(today)
    row_count = bsery.write_df_to_db(df)
    logger.info(f"写入了{row_count}条{__file__}策略数据")
    logger.info("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
