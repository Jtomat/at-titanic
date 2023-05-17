# Импорты: тестовый клиент и экземпляр самого приложения
from functions import AppFunctions
import pandas as pd


test_age_data_frame = pd.DataFrame({
    "PassengerId": [1, 2, 3, 5],
    "Pclass": [3, 1, 0, 2],
    "Name": ["Braund, Mr. Owen Harris", "Madison Braun", "Steve Craftson", "Harry Fox"],
    "Sex": ["male", "male", "female", "female"],
    "Age": [32, 20, 44, 35],
})


test_fare_data_frame = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris"],
    "Fare": [7.25]
})


def test_data_source_read():
    """
    Метод для проверки загрузки набора данных
    """
    instance = AppFunctions('./assets/data.csv')
    assert instance.dataFrame is not None


def test_find_men_by_age(test_data: pd.DataFrame = test_age_data_frame, age_min: int = 30, age_max: int = 40):
    """
    Метод для проверки поиска мужчин в возрастном диапозоне.
    """
    instance = AppFunctions()
    instance.dataFrame = test_data
    assert instance.find_men_by_age(age_min, age_max)["Name"][0] == "Braund, Mr. Owen Harris"


def test_get_names_by_fare(test_data: pd.DataFrame = test_fare_data_frame, fare: float = 7):
    """
    Метод для проверки имен пассажиров, стоймость билета которых выше указанной.
    """
    instance = AppFunctions()
    instance.dataFrame = test_data
    assert instance.get_names_by_fare(fare)["Name"][0] == "Braund, Mr. Owen Harris"


test_get_names_by_fare()
