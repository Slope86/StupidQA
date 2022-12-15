from argument import Argument


def test_delay_property():
    # Test if delay property returns correct value
    args = ["-d", "5"]
    argument = Argument(args)
    assert argument.delay == 5

    # Test if delay property returns default value if argument not provided
    args = []
    argument = Argument(args)
    assert argument.delay == 1


def test_print_property():
    # Test if print property returns correct value
    args = ["-np"]
    assert Argument(args).print is False

    # Test if print property returns True if argument not provided
    args = []
    assert Argument(args).print is True
