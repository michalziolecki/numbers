from typing import Union, Any

import pytest as pytest

from src.number_parser import check_number


@pytest.mark.parametrize("value,expected", [(100, 3), (999, 3), (-10, 2), (3.1415, 1)])
def test_check_number_if_correct_input(value: Union[int, float], expected: int) -> None:
    assert check_number(value) == expected


@pytest.mark.parametrize("value", ["100", complex(2, 2)])
def test_check_number_if_incorrect_input(value: Union[Any]) -> None:
    with pytest.raises(ValueError) as exc_info:
        check_number(value)  # type: ignore
    assert exc_info.value.args[0] == "integer or float required!"
