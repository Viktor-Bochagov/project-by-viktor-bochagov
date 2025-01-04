from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Маскирует информацию о картах и счетах"""

    if len(user_input.split()[-1]) == 16:
        new_card = get_mask_card_number(user_input.split()[-1])
        result = f"{user_input[:-16]}{new_card}"
    elif len(user_input.split()[-1]) == 20:
        new_card = get_mask_account(user_input.split()[-1])
        result = f"{user_input[:-20]}{new_card}"
    elif len(get_mask_card_number(user_input.split()[-1])) != 16:
        raise IndexError("Не соответствует длина строки номера карты")
    elif len(get_mask_account(user_input.split()[-1])) != 20:
        raise IndexError("Не соответствует длина строки номера счёта")
    return result


def get_date(date: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ"""

    if date == "":
        raise TypeError("Отсутствует обязательный аргумент")
    data_slize = date[0:10].split("-")
    return ".".join(data_slize[::-1])
