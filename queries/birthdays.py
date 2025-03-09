from typing import List
import structlog
import polars as pl
from query import Query

log = structlog.get_logger()

class Birthdays(Query):
    def run(self):
        try:
            log.info(f"running {__name__} query")
            super().run()
            df = pl.read_csv("testdata/birthdays.csv", schema={"Name": pl.String, "Birth Date": pl.Date})
            df.write_parquet("data/birthdays.parquet")
        except Exception as e:
            log.error(f"ec2a0ede-535a-4880-a48c-f72a7ef0bbc7 {e}")
