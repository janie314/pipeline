from typing import Any, Tuple
import polars as pl
import structlog

log = structlog.get_logger()


def query() -> Tuple[bool, Any]:
    try:
        df = pl.read_csv("testdata/customers.csv")
        filtered_df = df.filter(pl.col("First Name").str.starts_with("J"))
        return (True, filtered_df.head(10))
    except Exception as e:
        log.error(f"1993ed2c-905e-4b30-9268-94640042fa59: {e}")
        return (False, None)


if __name__ == "__main__":
    (ok, res) = query()
    if ok:
        print(res)
    else:
        log.error("bombed out...")
