from typing import Any, Dict, Iterable


def filter_by_currency(list_dict_check: Iterable[Dict], value_key: str = "USD") -> Iterable[Dict]:
    """Функция которая, принимает на вход список словарей, представляющих транзакции и даёт итератор с валютой 'USD'"""

    for check_dict in list_dict_check:
        if (check_dict["operationAmount"]["currency"]["code"]) == value_key:
            yield check_dict
        elif (check_dict["operationAmount"]["currency"]["code"]) == "RUB":
            continue
        elif (check_dict["operationAmount"]["currency"]["code"]) != value_key:
            raise TypeError("Не соответствует заданной валюте")
