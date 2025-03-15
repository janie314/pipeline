import polars as pl
from query import Query


def birthdays_query(dependency_results):
    df = pl.read_csv("testdata/birthdays.csv").select(
        pl.col("Name"),
        pl.col("Birth Date").str.to_date("%B%e, %Y", strict=False),
    )
    return df


def birthdays():
    return Query(name="birthdays", dependencies=[], query_method=birthdays_query)
