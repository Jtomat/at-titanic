import pandas as pd


class AppFunctions(object):
    dataFrame: pd.DataFrame
    
    def __init__(self, source: str = None):
        if source is not None:
            self.dataFrame = pd.read_csv(source)
        else:
            self.dataFrame = pd.DataFrame()
    
    def find_men_by_age(self, age_min: int, age_max: int) -> pd.DataFrame:
        if age_max > 60 or age_min < 30:
            return Exception('Age out of range [30; 60]')
        data_slice: pd.DataFrame = self.dataFrame \
            .loc[(self.dataFrame['Sex'] == 'male') &
                 (self.dataFrame['Age'] >= age_min) &
                 (self.dataFrame['Age'] <= age_max)]
        return data_slice[['Name', 'Age', 'Pclass']]
    
    def get_names_by_fare(self, fare: int) -> pd.DataFrame:
        data_slice: pd.DataFrame = self.dataFrame.loc[self.dataFrame["Fare"] > fare]
        return data_slice[["Name"]]
    
    def find_passengers_by_name_start(self, name_start: str) -> pd.DataFrame:
        data_slice: pd.DataFrame = self.dataFrame \
            .loc[self.dataFrame['Name'].str.startswith(name_start)]
        return data_slice[['Name', 'Age', 'Pclass']]
