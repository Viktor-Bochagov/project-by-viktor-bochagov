from typing import Dict, Iterable


def filter_by_currency(list_dict_check: Iterable[Dict], value_key: str = "USD") -> Iterable[Dict]:
    """Функция которая, принимает на вход список словарей, представляющих транзакции и даёт итератор с валютой 'USD'"""

    for check_dict in list_dict_check:
        if (check_dict["operationAmount"]["currency"]["code"]) == value_key:
            yield check_dict
        elif (check_dict["operationAmount"]["currency"]["code"]) == "RUB":
            continue
        elif (check_dict["operationAmount"]["currency"]["code"]) != value_key:
            raise TypeError("Не соответствует заданной валюте")


def transaction_descriptions(list_dict: Iterable[Dict], key: str = "description") -> Iterable[Dict]:
    """Функция который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    for check_key in list_dict:
        if key in check_key:
            yield check_key[key]
        elif not check_key.get(key):
            raise TypeError("Отсутствует строка")