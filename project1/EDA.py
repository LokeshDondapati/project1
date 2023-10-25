import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# dataset url

url = 'https://raw.githubusercontent.com/LokeshDondapati/project1/main/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv'


class EDA:
    """
            class to get data from url and to showcase data.
            show Summary of statistics
             stored in a DataFrame called "summary_stats."

            Parameters:
            - url (str): url of dataset."""

    def __init__(self):
        self.url = url

    def readdata(self, url):
        """For loading dataset, datset was uploaded to GitHub and with the gitHub url all  the data is being fetched"""
        data = pd.read_csv(self.url)
        return data

    def statistics(self):
        """Summary statistics for dataframe are calculated with describe func"""
        # Method readdata is called for data fetch
        summary_stats = self.readdata(url).describe(include='all')
        return summary_stats

    def graphical_analysis_matplotlib_year(self):
        """
            dimensions/size are given 8,6 and colour as skyblue for matplotlib histogram.

            Graph axis:
            - X: Year.
            - Y: Frequency.

            Returns:
            Histogram of year.
            """
        plt.figure(figsize=(8, 6))
        # Method readdata is used here for year
        plt.hist(self.readdata(url)['YEAR'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('YEAR')
        plt.ylabel('Frequency')
        plt.title('Histogram for YEAR')
        result = plt.show()
        return result

    def graphical_analysis_matplotlib_age(self):
        """
                    dimensions/size are given 8,6 and colour as sky blue for matplotlib histogram.

                    Graph axis:
                    - X: age.
                    - Y: Frequency.

                    Returns:
                    Histogram of age.
                    """
        plt.hist(self.readdata(url)['AGE'], bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('AGE')
        plt.ylabel('Frequency')
        plt.title('Histogram for AGE')
        result = plt.show()
        return result

    def graphical_analysis_seaborn_year(self):
        """
                    dimensions/size are given 8,6 and colour as sky blue for seaborn histogram.

                    Graph axis:
                    - X: Year.
                    - Y: Frequency.

                    Returns:
                    Histogram of year.
                    """
        plt.figure(figsize=(8, 6))

        sns.histplot(self.readdata(url)['YEAR'], bins=30, color='blue', kde=True)
        plt.xlabel('YEAR')
        plt.ylabel('Frequency')
        plt.title('Histogram for YEAR')
        result = plt.show()
        return result

    def graphical_analysis_seaborn_age(self):
        """
                    dimensions/size are given 8,6 and colour as sky blue for seaborn histogram.

                    Graph axis:
                    - X: age.
                    - Y: Frequency.

                    Returns:
                    Histogram of age.
                    """
        sns.histplot(self.readdata(url)['AGE'], bins=30, color='blue', kde=True)
        plt.xlabel('AGE')
        plt.ylabel('Frequency')
        plt.title('Histogram for AGE')
        result = plt.show()
        return result
        # return histogram

