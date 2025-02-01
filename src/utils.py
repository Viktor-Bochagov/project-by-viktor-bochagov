import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def operation(open_file: Any) -> Any:
    """Принимает на вход имя JSON-файла по пути ./data/ и
    возвращает список словарей с данными о финансовых транзакциях"""

    open_file += ".json"
    try:
        logger.info(
            f"Данная функция {operation.__name__} принимает на вход имя JSON-файла и возвращает список словарей"
        )
        with open(DATA_DIR / open_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        logger.error(f"Произошла ошибка типа {e}")
        print(f"Ошибка {e}")
        return []
    except FileNotFoundError as e:
        logger.error(f"Произошла ошибка: Файл не найден {e}")
        print(f"Ошибка: Файл не найден {e}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Произошла ошибка декодирования файла {e}")
        print(f"Ошибка декодирования файла {e}")
        return []
    return data
