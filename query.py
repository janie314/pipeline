
from typing import List

class Query:
    def __init__(self, dependencies: List['Query']):
        self.dependencies = dependencies

    def run(self):
        for dep in self.dependencies:
            dep.run()