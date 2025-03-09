import structlog
import polars as pl
from query import Query

log = structlog.get_logger()


class CustomersBdaysCollated(Query):
    def run(self):
        try:
            log.info(f"running {__name__} query")
            super().run()
            df = pl.read_csv("testdata/customers.csv")
            filtered_df = df.filter(pl.col("First Name").str.starts_with("J"))
            filtered_df.head(10).write_parquet("data/customers.parquet")
        except Exception as e:
            log.error(f"474a979f-c4ce-49d2-9bd4-04e3ad50bad6 {e}")
