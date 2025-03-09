import structlog
import polars as pl

log = structlog.get_logger()

def customers() -> bool:
    df = pl.read_csv("testdata/customers.csv")
    filtered_df = df.filter(pl.col("First Name").str.starts_with("J"))
    return filtered_df.head(10)
