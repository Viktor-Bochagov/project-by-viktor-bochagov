import json
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def operation(open_file: Any) -> Any:
    """Принимает на вход имя JSON-файла по пути ./data/ и
    возвращает список словарей с данными о финансовых транзакциях"""

    open_file += ".json"
    try:
        with open(DATA_DIR / open_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка {e}")
        return []
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования файла {e}")
        return []
    return data
