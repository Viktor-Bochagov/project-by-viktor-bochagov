from src.utils import operation


def test_operation(mock_operation_json_file):
    transactions = operation("operations")
    assert len(transactions) == 101
