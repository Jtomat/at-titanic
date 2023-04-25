import pandas as pd


class app_functions:
    dataFrame: pd.DataFrame

    def __init__(self):
        self.dataFrame = pd.read_csv('./assets/data.csv')

    def find_men_by_age(self, age: int) -> pd.DataFrame:
        if age > 60 or age < 30:
            return Exception('Age out of range [30; 60]');
        data_slice: pd.DataFrame = self.dataFrame.loc[self.dataFrame['Sex'] == 'male'].loc[
            self.dataFrame['Age'] == age]
        return data_slice[['Name', 'Age', 'Pclass']]

    def get_names(self, fare: int) -> pd.DataFrame:
        data_slice: pd.DataFrame = self.dataFrame.loc[self.dataFrame["Fare"] > fare]
        return data_slice[["Name"]]
