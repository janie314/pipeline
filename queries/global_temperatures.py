import polars as pl
import altair as alt
from query import Query


def global_temperatures_query(dependency_results):
    df = pl.read_csv("testdata/global_temperatures.csv")
    return df


def global_temperatures():
    df = Query(
        name="global_temperatures",
        dependencies=[],
        query_method=global_temperatures_query,
    ).run()
    alt.Chart(df).mark_point().encode(
        x="LandMaxTemperature", y="LandMinTemperature"
    ).save("data/global_temperatures_min_vs_max.svg")
    return df
