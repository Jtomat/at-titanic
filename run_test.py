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
