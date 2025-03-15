import structlog
from queries.customers_bdays_collated import customers_bdays_collated

log = structlog.get_logger()

if __name__ == "__main__":
    log.info("starting the data pipeline")
    customers_bdays_collated().run()
