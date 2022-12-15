# Description: Parse arguments from command line.
import argparse


class Argument:
    """A class for handling command line arguments.

    This class uses the argparse module to parse command line arguments.
    Uses property methods, 'delay' and 'print', to return the corresponding argument values.

    Arguments:
        -d or --delay: an integer representing the delay between Google search requests, default = 1.
        -np or --no-print: not print the QA process.
    """

    _default_args = None

    def __init__(self, args=None):
        if args is None and Argument._default_args is not None:
            self._args = Argument._default_args
            return
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d", "--delay", type=int, default=1, help="Delay between Google search requests, default = 1"
        )
        parser.add_argument(
            "-np", "--no-print", action="store_false", dest="print", help="Will not print the QA process"
        )
        self._args = parser.parse_args(args)
        if Argument._default_args is None:
            Argument._default_args = self._args

    @property
    def delay(self) -> int:
        return self._args.delay

    @property
    def print(self) -> bool:
        return self._args.print
