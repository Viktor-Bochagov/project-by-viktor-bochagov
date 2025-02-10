import logging
import os
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\logs\\masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
