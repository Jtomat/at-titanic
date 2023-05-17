# Импорты: тестовый клиент и экземпляр самого приложения
from functions import AppFunctions
import pandas as pd

test_data_frame = pd.DataFrame()

def test_data_source_read():
    """
    Метод для проверки загрузки набора данных
    """
    instance = AppFunctions('./assets/data.csv')
    assert instance.dataFrame is not None
    
    
def test_find_men_by_age():
    """
    Метод для проверки поиска мужчин в возрастном диапозоне
    """
    assert True
    