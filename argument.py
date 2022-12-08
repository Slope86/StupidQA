# Description: Parse arguments from command line.
import argparse


class Argument:
    """
    Parse arguments from command line.

    This class uses the `argparse` module to parse arguments passed to the program on the command line.
    It defines two optional arguments:

    - "-d" or "--delay": Set the delay between Google search requests. The default value is 1.
    - "-np" or "--no-print": Do not print the QA process.

    The parsed arguments are saved as attributes of the class, and can be accessed by other parts of the program.

    This class also uses the Singleton pattern to ensure that only one instance of ArgumentParser is created.

    Example:
        args = Argument()
        delay = args.delay
        should_print = args.print
    """

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
        parser.add_argument(
            "-np", "--no-print", action="store_false", dest="print", help="Will not print the QA process"
        )
        args = parser.parse_args()

        # Save arguments as attributes
        cls.delay: int = args.delay
        cls.print: bool = args.print
        return cls._instance
