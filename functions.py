import pandas as pd


class app_functions:
    dataFrame: pd.DataFrame;
    
    def __init__(self):
        self.dataFrame = pd.read_csv('./assets/titanic.csv');
        
    def find_men_by_age(self, age: int) -> pd.DataFrame:
        data_slice: pd.DataFrame = self.dataFrame.loc[self.dataFrame['Sex'] == 'male'].loc[self.dataFrame['Age'] == age];
        return data_slice[['Name', 'Age', 'Pclass']];