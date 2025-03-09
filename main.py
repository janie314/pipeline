from typing import Any, Tuple
from queries.customers import Customers
from queries.birthdays import Birthdays

if __name__ == "__main__":
    Customers([Birthdays([])]).run()