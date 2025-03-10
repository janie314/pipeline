import polars as pl
from query import Query


def customer_query(dependency_results):
    df = pl.read_csv("testdata/customers.csv").with_columns(
        pl.col("Subscription Date").str.to_date("%Y-%m-%d", strict=False)
    )
    filtered_df = df.filter(pl.col("First Name").str.starts_with("J"))
    return filtered_df


def customers():
    return Query(name="customers", dependencies=[], query_method=customer_query)
