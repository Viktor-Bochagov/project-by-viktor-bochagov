import os
from unittest.mock import patch

import pandas as pd

from src.read_mod import read_csv, read_excel


@patch("csv.DictReader")
def test_read_csv(mock_datafiles):
    mock_datafiles.return_value = [{"test": "1"}]
    assert (read_csv(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\transactions.csv") ==
            [{"test": "1"}])


def test_reader_from_csv_not_files():
    assert read_csv(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\qwerty.csv") == []


@patch("pandas.read_excel")
def test_reader_from_excel(mock_datafiles):
    mock_datafiles.return_value = pd.DataFrame({"test": ["1"]})
    assert (read_excel(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\transactions_excel.xlsx")
            == [{"test": "1"}])


def test_reader_from_excel_not_files():
    assert read_csv(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\qwerty.csv") == []
