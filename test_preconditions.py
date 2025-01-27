import allure
import pytest

@pytest.fixture
def prepare_data():
    print("Подготовка данных")
    data = {"key": "value"}
    yield data
    print("Очистка данных после теста")

def test_with_yield_fixture(prepare_data):
    assert prepare_data["key"] == "value"