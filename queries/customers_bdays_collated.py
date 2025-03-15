from queries.birthdays import birthdays
from queries.customers import customers
from query import Query
from polars import col as C


def customers_bdays_collated_query(dependency_results):
    [birthdays_res, customers_res] = dependency_results
    return birthdays_res.with_columns(
        C("Birth Date").dt.strftime("%m-%d").alias("birthday")
    ).join(
        customers_res.with_columns(
            C("Subscription Date").dt.strftime("%m-%d").alias("birthday")
        ),
        on="birthday"
    )


def customers_bdays_collated():
    return Query(
        name="customer_bdays_collated",
        dependencies=[birthdays(), customers()],
        query_method=customers_bdays_collated_query,
    )
