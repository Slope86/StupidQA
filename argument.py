# Description: Parse arguments from command line.
import argparse


class Argument:
    """A class for handling command line arguments.

    This class uses the argparse module to parse command line arguments.
    Uses property methods, 'delay' and 'print', to return the corresponding argument values.
    Uses singleton to ensure only one instance of ArgumentParser is created.

    Arguments:
        -d or --delay: an integer representing the delay between Google search requests, default = 1.
        -np or --no-print: not print the QA process.
    """

    def __new__(cls, args=None):
        # Singleton
        if hasattr(cls, "_instance"):
            return cls._instance

        # Parse arguments
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d", "--delay", type=int, default=1, help="Delay between Google search requests, default = 1"
        )
        parser.add_argument(
            "-np", "--no-print", action="store_false", dest="print", help="Will not print the QA process"
        )
        cls._args = parser.parse_args(args)
        cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def delay(cls) -> int:
        return cls._args.delay

    @property
    def print(cls) -> bool:
        return cls._args.print
