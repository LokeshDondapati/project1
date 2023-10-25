import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datasummary import Datasummary

url = 'https://raw.githubusercontent.com/LokeshDondapati/project1/main/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv'
v=Datasummary(url)
f=v.readdata(url)
class EDA:
    def __init__(self):
        self.data = f

    def statistics(self):
        summary_stats_numeric = self.data.describe(include=['float64', 'int64'])
        print(summary_stats_numeric)

        summary_stats = self.data.describe(include='all')
        print(summary_stats)
    def graphical_analysis_matplotlib(self):
        plt.figure(figsize=(8, 6))

        plt.hist(self.data['YEAR'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('YEAR')
        plt.ylabel('Frequency')
        plt.title('Histogram for YEAR')
        plt.show()
        plt.hist(self.data['AGE'], bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('AGE')
        plt.ylabel('Frequency')
        plt.title('Histogram for AGE')
        plt.show()
    def graphical_analysis_seaborn(self):
        plt.figure(figsize=(8, 6))

        sns.histplot(self.data['YEAR'], bins=30, color='blue', kde=True)
        plt.xlabel('YEAR')
        plt.ylabel('Frequency')
        plt.title('Histogram for YEAR')
        plt.show()
        sns.histplot(self.data['AGE'], bins=30, color='blue', kde=True)
        plt.xlabel('AGE')
        plt.ylabel('Frequency')
        plt.title('Histogram for AGE')
        plt.show()




if __name__ == "__main__":
    output = EDA()
    v = output.statistics()
    x=output.graphical_analysis_seaborn()
