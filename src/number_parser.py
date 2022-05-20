from typing import Union


def check_number(value: Union[int, float]) -> int:
    if not any([isinstance(value, req_type) for req_type in {int, float}]):
        raise ValueError("integer or float required!")

    casted_value: int = int(value)
    absolute_value = abs(casted_value)
    return len(f"{absolute_value}")
