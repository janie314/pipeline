import os
import structlog
from typing import List

log = structlog.get_logger()


class Query:
    def __init__(self, dependencies: List["Query"]):
        self.dependencies = dependencies

    def run(self):
        os.makedirs(os.path.join(os.path.dirname(__file__), "data"), exist_ok=True)
        for dep in self.dependencies:
            dep.run()
