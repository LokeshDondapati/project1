# importing library pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/LokeshDondapati/project1/main/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv'


class Datasummary:
    def __init__(self, url):
        self.url = url

    def readdata(self,url):
        """For loading dataset, datset was uploaded to GitHub and with the gitHub url all  the data is being fetched"""
        data = pd.read_csv(self.url)
        return data

    def datasummary(self):
        data = self.readdata(url)
        # Calculate the number of use cases
        num_use_cases = data.shape[0]

        # Calculate the number of attributes
        num_attributes = data.shape[1]

        # List data types for each attribute
        data_types = data.dtypes

        # Display the results
        print("Use Cases:", num_use_cases)
        print("Attributes:", num_attributes)
        print("Data Types for Attribute:", data_types)
        result ={"Use Cases": num_use_cases, "Attributes": num_attributes, "Data Types for Attribute": data_types}
        return result

if __name__ == "__main__":
    output = Datasummary(url=url)
    v = output.datasummary()
