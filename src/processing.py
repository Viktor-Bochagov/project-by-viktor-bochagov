from typing import Dict, List


def filter_by_state(last_dict: List[Dict], value_key: str = "EXECUTED") -> List[Dict]:
    """Возвращает новый список словарей, содержащий словари соответствующих ключ"""

    new_list_dict = []
    for every_dict in last_dict:
        if every_dict["state"] == value_key:
            new_list_dict.append(every_dict)
    return new_list_dict


def sort_by_date():
    pass