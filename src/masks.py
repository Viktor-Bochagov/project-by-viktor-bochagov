from typing import Union


def get_mask_card_number(card_num: Union[str]) -> str:
    """Возвращает маску номера по правилу XXXX XX ** **** XXXX"""

    if card_num == "":
        raise TypeError("Отсутствует обязательный аргумент при вводе номера карты")
    elif len(card_num) != 16:
        raise IndexError("Не соответствует длина строки номера карты")
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(account: Union[str]) -> str:
    """Возвращает маску номера по правилу **XXXX"""

    if account == "":
        raise TypeError("Отсутствует обязательный аргумент при вводе номера счёта")
    elif len(account) != 20:
        raise IndexError("Не соответствует длина строки номера счёта")
    return f"**{account[-4:]}"
