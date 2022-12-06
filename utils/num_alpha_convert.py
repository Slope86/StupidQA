def Num2Alpha(num: int) -> str:
    if 1 <= num <= 26:
        return chr(num + 64)
    raise ValueError(f"num must be in range(1, 27), but got {num}")


def Alpha2Num(alphabet: str) -> int:
    if len(alphabet) != 1:
        raise ValueError(f"alphabet must be a single character, but got {alphabet}")

    num = ord(alphabet.upper()) - 64
    if 1 <= num <= 26:
        return num
    else:
        raise ValueError(f"alphabet must be in range(1, 27), but got {alphabet}")


def NumAlphaConvert(arg: int | str) -> str | int:
    """Convert number to alphabet or alphabet to number

    Raises:
        TypeError: arg is not int or str
        ValueError: arg is not in range(1, 27) or is not a alphabet

    Returns:
        int or str
    """
    if isinstance(arg, int):
        return Num2Alpha(arg)
    if isinstance(arg, str):
        return Alpha2Num(arg)
    raise TypeError(f"arg must be int or str, but got {type(arg)}")
