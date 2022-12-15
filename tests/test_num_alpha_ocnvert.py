import pytest

from utils.num_alpha_convert import NumAlphaConvert


def test_NumAlphaConvert():
    # Test converting number to alphabet
    assert NumAlphaConvert(1) == "A"
    assert NumAlphaConvert(26) == "Z"

    # Test converting alphabet to number
    assert NumAlphaConvert("A") == 1
    assert NumAlphaConvert("Z") == 26

    # Test converting invalid number
    with pytest.raises(ValueError, match=r"num must be in range\(1, 27\), but got 0"):
        NumAlphaConvert(0)
    with pytest.raises(ValueError, match=r"num must be in range\(1, 27\), but got 27"):
        NumAlphaConvert(27)

    # Test converting invalid alphabet
    with pytest.raises(ValueError, match=r"alphabet must be a single character, but got ABC"):
        NumAlphaConvert("ABC")

    # Test converting invalid type
    with pytest.raises(TypeError, match=r"arg must be int or str, but got <class 'float'>"):
        NumAlphaConvert(1.5)  # type: ignore
    with pytest.raises(TypeError, match=r"arg must be int or str, but got <class 'list'>"):
        NumAlphaConvert([1, 2, 3])  # type: ignore
