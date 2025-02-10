# Виджет банковских операций

Проект "Виджет" - это консоль приложение на Python для банковских операций клиента.
В проекте реализована функция маскировки номера карты и номера счёта — mask_account_card и функционал по сортировке банковских операций клиента
# Модуль main

Отвечает за основную логику проекта и связывает функциональности между собой.


# Добавлен новый модуль dictonary_search в пакет src:
Реализована функция, которая принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей, у которых в описании есть данная строка

Реализована функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории

# Добавлен новый модуль read_mod в пакет src:
Реализованна новая функция read_csv которая принимает в качестве аргумента путь к csv-файлу и возвращает его содержимое в виде списка словарей

Реализованна новая функция read_excel которая принимает в качестве аргумента путь к excel-файлу и возвращает его содержимое в виде списка словарей

Так же добавлена нова директория 'data2' для хранения файлов transactions.csv и transactions.xlsx

# Добавлен новый модуль generators.py в пакет src

Функция filter_by_currency:
Функция которая, принимает на вход список словарей, представляющих транзакции и возвращает итератор с соответствующей валютой 'USD'.

Функция transaction_descriptions:
Функция который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

Функция card_number_generator:
Функция-генератор которая принимает начальное и конечное значения для генерации диапазона номеров.

# Добавлен новый модуль decorators.py в пакет src

Декоратор 'log' автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.

# Тестирование:

Добавлены модули с тестами по всем модулям из папки src.
Протестированы разные сценарий формата ввода и вывода.
 * Для запуска тестов пропишите в консоль:
   ```bash
   pytest
   ```
## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_репозиторий.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd ваш_проект
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Примеры использования функций:

```python
from src.decorators import my_function
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Пример использования mask_account_card
mask_account_card("Visa Platinum 7000792289606361")

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)

# Пример использования модуля generators
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)


descriptions = transaction_descriptions(transactions, "description")
for description in descriptions:
    print(description)

for card in card_number_generator(1, 6):
    print(card)

# Пример использования декоратора log
my_function(1, 3)
my_function(4, 3)
```
