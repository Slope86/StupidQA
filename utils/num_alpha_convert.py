def _Num2Alpha(num: int) -> str:
    if 1 <= num <= 26:
        return chr(num + 64)
    raise ValueError


def _Alpha2Num(alphabet: str) -> int:
    if len(alphabet) != 1:
        raise ValueError

    num = ord(alphabet.upper()) - 64
    if 1 <= num <= 26:
        return num
    else:
        raise ValueError


def NumAlphaConvert(arg: int | str) -> str | int:
    """Convert number to alphabet or alphabet to number

    Raises:
        TypeError: arg is not int or str
        ValueError: arg is not in range(1, 27) or is not a alphabet

    Returns:
        int or str
    """
    if isinstance(arg, int):
        return _Num2Alpha(arg)
    if isinstance(arg, str):
        return _Alpha2Num(arg)
    raise TypeError
