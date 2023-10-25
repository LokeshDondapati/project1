# import of pandas, seaborn, matplotlib libraries
import pandas as pd
import numpy as np
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
        age, NEIGHBORHOOD, and RACE/ETHNICITY interact in influencing HIV/AIDS diagnoses
        :return: graphical analysis for Interaction of Age, NEIGHBORHOOD, and RACE/ETHNICITY in HIV/AIDS Diagnoses
        """
        data = self.readdata(url)

        # Clean the 'TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES' column by replacing '000*' with NaN
        data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'] = pd.to_numeric(
            data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'].replace('000*', None, regex=True), errors='coerce')

        # Create a pivot table to capture the interaction
        pivot_table = data.pivot_table(index='AGE', columns=['NEIGHBORHOOD', 'RACE/ETHNICITY'],
                                       values='TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES', aggfunc='sum')
        """
                                   dimensions/size are given 16,8 for seaborn histogram.

                                   Graph axis:
                                   - X: NEIGHBORHOOD, RACE/ETHNICITY.
                                   - Y: age.

                                   Returns:
                                            graphical analysis for Interaction of Age, NEIGHBORHOOD, and RACE/ETHNICITY in HIV/AIDS Diagnoses.
                                   """

        # Plotting the heatmap
        plt.figure(figsize=(16, 8))
        sns.barplot(x='AGE', y='TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES', hue='RACE/ETHNICITY', data=data,
                    palette='viridis')
        plt.title('Interaction of Age, NEIGHBORHOOD, and RACE/ETHNICITY in HIV/AIDS Diagnoses')
        plt.xlabel('NEIGHBORHOOD, RACE/ETHNICITY')
        plt.ylabel('AGE')
        result = plt.show()
        return result

    def analysis_matplotlib(self):
        """
                age, NEIGHBORHOOD, and RACE/ETHNICITY interact in influencing HIV/AIDS diagnoses
                :return: graphical analysis for Interaction of Age, NEIGHBORHOOD, and RACE/ETHNICITY in HIV/AIDS Diagnoses
                """
        data = self.readdata(url)
        # Clean the 'Number of Diagnoses' column by replacing '000*' with NaN
        data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'] = pd.to_numeric(
            data['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'].replace('000*', None, regex=True),
            errors='coerce')

        # Create a pivot table to capture the interaction
        pivot_table = data.pivot_table(index='AGE', columns=['NEIGHBORHOOD', 'RACE/ETHNICITY'],
                                       values='TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES', aggfunc='sum')

        # Plotting the heatmap using matplotlib
        plt.figure(figsize=(16, 16))
        """
                                           dimensions/size are given 16,16 for seaborn histogram.

                                           Graph axis:
                                           - X: NEIGHBORHOOD, RACE/ETHNICITY.
                                           - Y: age.

                                           Returns:
                                                    graphical analysis for Interaction of Age, NEIGHBORHOOD, and RACE/ETHNICITY in HIV/AIDS Diagnoses.
                                           """
        # In sns heatmp was used and imshow is used for matpotlib
        plt.imshow(pivot_table, cmap='viridis', aspect='auto', interpolation='nearest')
        plt.colorbar(label='TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES')
        plt.title('Interaction of Age, NEIGHBORHOOD, and RACE/ETHNICITY in HIV/AIDS Diagnoses (matplotlib)')
        plt.xlabel('NEIGHBORHOOD, RACE/ETHNICITY')
        plt.ylabel('Age Group')
        plt.xticks(np.arange(pivot_table.shape[1]), pivot_table.columns.get_level_values(1), rotation=45, ha='right')
        plt.yticks(np.arange(pivot_table.shape[0]), pivot_table.index)
        result = plt.show()
        return result


# not in use
"""if __name__ == "__main__":
    output = Inference()
    v = output.analysis_seaborn()
"""
