import os
import structlog
from typing import List

log = structlog.get_logger()


class Query:
    def __init__(self, name: str, dependencies: List["Query"], query_method):
        self.name = name
        self.dependencies = dependencies
        self.query_method = query_method

    def run(self):
        log.info(f"running {self.name} query")
        os.makedirs(os.path.join(os.path.dirname(__file__), "data"), exist_ok=True)
        dependency_results = [dep.run() for dep in self.dependencies]
        df = self.query_method(dependency_results)
        outpath = os.path.join("data", f"{self.name}.parquet")
        log.info(f"writing query results to {outpath}")
        df.write_parquet(outpath)
        outpath = os.path.join("data", f"{self.name}.csv")
        log.info(f"writing query results to {outpath}")
        df.write_csv(outpath)
        return df
