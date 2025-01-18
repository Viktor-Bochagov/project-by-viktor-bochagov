import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(list_dict_check) -> None:
    generator = filter_by_currency(list_dict_check)
    assert next(generator)


def test_filter_by_currency_negative() -> None:
    with pytest.raises(TypeError, match="Не соответствует заданной валюте"):
        list(filter_by_currency([{"operationAmount": {"currency": {"code": ""}}}], " "))
