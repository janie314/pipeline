from queries.birthdays import birthdays
from queries.customers import customers
from query import Query


def customers_bdays_collated_query(dependency_results):
    [birthdays_res, customers_res] = dependency_results
    return birthdays_res.join(
        customers_res, left_on="Birth Date", right_on="Subscription Date", how="left"
    )


def customers_bdays_collated():
    return Query(
        name="customer_bdays_collated",
        dependencies=[birthdays(), customers()],
        query_method=customers_bdays_collated_query,
    )
