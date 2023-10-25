import pandas as pd
#import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# dataset url
url = 'https://raw.githubusercontent.com/LokeshDondapati/project1/main/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv'


class Inference:
    def __init__(self):
        self.url = url

    def readdata(self, url):
        """For loading dataset, datset was uploaded to GitHub and with the gitHub url all  the data is being fetched"""
        data = pd.read_csv(self.url)
        return data

    def analysis_seaborn(self):
        """
                 finding specific age groups with higher or lower diagnosis rates
                :return: 'Mean of HIV/AIDS Diagnoses by AGE (seaborn)

                """
        # readdata method for fetching data
        data = self.readdata(url)

        # Cleaning the 'TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES' column by replacing '000*' with NaN
        data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'] = pd.to_numeric(
            data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'].replace('000*', None, regex=True),
            errors='coerce')

        # Calculate mean diagnosis rate for each AGE
        mean_diagnosis_by_age = data.groupby('AGE')[
            'TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'].mean().reset_index()

        """
                           dimensions/size are given 12,6 for seaborn histogram.

                           Graph axis:
                           - X: age.
                           - Y: Mean of TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES.

                           Returns:
                                    Mean of graphical analysis to know higher of lower daignoses rates.
                           """

        # Plot using seaborn
        plt.figure(figsize=(12, 6))
        sns.barplot(x='AGE', y='TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES', data=mean_diagnosis_by_age,
                    palette='viridis')
        plt.title('Mean of HIV/AIDS Diagnoses by AGE (seaborn)')
        plt.xlabel('AGE')
        plt.ylabel('Mean of TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES')
        result = plt.show()
        return result

    def analysis_matplotlib(self):
        """
                         finding specific age groups with higher or lower diagnosis rates
                        :return: 'Mean of HIV/AIDS Diagnoses by AGE (matplotlib)

                        """
        data = self.readdata(url)
        # Clean the 'TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES' column by replacing '000*' with NaN
        data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'] = pd.to_numeric(
            data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'].replace('000*', None, regex=True),
            errors='coerce')

        # Calculate mean diagnosis rate for each AGE
        mean_diagnosis_by_age = data.groupby('AGE')[
            'TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'].mean().reset_index()
        """
                                   dimensions/size are given 12,6 for matplotlib histogram.

                                   Graph axis:
                                   - X: age.
                                   - Y: Mean of TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES.

                                   Returns:
                                    Mean of graphical analysis to know higher of lower daignoses rates.
                                   """

        # Plotting using matplotlib
        plt.figure(figsize=(12, 6))

        plt.bar(mean_diagnosis_by_age['AGE'], mean_diagnosis_by_age['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'],
                color='skyblue')
        plt.title('Mean HIV/AIDS Diagnoses by AGE (matplotlib)')
        plt.xlabel('AGE')
        plt.ylabel('Mean TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES')
        result = plt.show()
        return result


if __name__ == "__main__":
    output = Inference()
    v = output.analysis_matplotlib()
    output.analysis_seaborn()
