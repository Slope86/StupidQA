# Description: Parse arguments from command line
import argparse


class Argument:
    """Parse arguments from command line."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d", "--delay", type=int, default=1, help="Delay between Google search requests, default = 1"
        )
        parser.add_argument("-np", "--no-print", action="store_false", dest="print", help="don't print the QA process")
        args = parser.parse_args()
        self.delay: int = args.delay
        self.print: bool = args.print
