import logging
from typing import Union

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/mask.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_num: Union[str]) -> str:
    """Возвращает маску номера по правилу XXXX XX ** **** XXXX"""

    logger.info(f"Данная функция {get_mask_card_number.__name__} маскирует номер карты по типу 1234 56** **** 4567")
    if card_num == "":
        logger.error(f"Произошла ошибка типа {TypeError}: отсутствует аргумент ввода")
        raise TypeError("Отсутствует обязательный аргумент при вводе номера карты")
    elif len(card_num) != 16:
        logger.error(f"Произошла ошибка типа {IndexError}: не соответствует длина строки")
        raise IndexError("Не соответствует длина строки номера карты")
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(account: Union[str]) -> str:
    """Возвращает маску номера по правилу **XXXX"""

    logger.info(f"Данная функция {get_mask_account.__name__} маскирует номер счёта по типу **1234")
    if account == "":
        logger.error(f"Произошла ошибка типа {TypeError}: отсутствует аргумент ввода")
        raise TypeError("Отсутствует обязательный аргумент при вводе номера счёта")
    elif len(account) != 20:
        logger.error(f"Произошла ошибка типа {IndexError}: не соответствует длина строки")
        raise IndexError("Не соответствует длина строки номера счёта")
    return f"**{account[-4:]}"
