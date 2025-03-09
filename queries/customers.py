from typing import List
import structlog
import polars as pl
from query import Query

log = structlog.get_logger()

class Customers(Query):
    def run():
        try:
            super()
            log.info(f"running {__name__} query")
            df = pl.read_csv("testdata/customers.csv")
            filtered_df = df.filter(pl.col("First Name").str.starts_with("J"))
            filtered_df.head(10).write_parquet("data/customers.parquet")
        except Exception as e:
            log.error(f"{e}")
