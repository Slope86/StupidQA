# Description: Parse arguments from command line
import argparse


class Argument:
    """Parse arguments from command line."""

    def __new__(cls):
        # Singleton
        if hasattr(cls, "_instance"):
            return cls._instance
        cls._instance = super().__new__(cls)

        # Parse arguments
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d", "--delay", type=int, default=1, help="Delay between Google search requests, default = 1"
        )
        parser.add_argument("-np", "--no-print", action="store_false", dest="print", help="don't print the QA process")
        args = parser.parse_args()

        # Save arguments in attributes
        cls.delay: int = args.delay
        cls.print: bool = args.print
        return cls._instance
