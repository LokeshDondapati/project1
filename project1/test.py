import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://raw.githubusercontent.com/LokeshDondapati/project1/main/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv'
df = pd.read_csv(url)

# Clean the 'TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES' column by replacing '000*' with NaN
df['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'] = pd.to_numeric(df['TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES'].replace('000*', None, regex=True), errors='coerce')

# Create a pivot table to capture the interaction
pivot_table = df.pivot_table(index='AGE', columns=['NEIGHBORHOOD', 'RACE/ETHNICITY'], values='TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES', aggfunc='sum')

# Plotting the heatmap
plt.figure(figsize=(16, 8))
sns.barplot(x='AGE', y='TOTAL NUMBER OF CONCURRENT HIV/AIDS DIAGNOSES', hue='RACE/ETHNICITY', data=df, palette='viridis')
plt.title('Interaction of Age, Neighborhood, and Race/Ethnicity in HIV/AIDS Diagnoses')
plt.xlabel('NEIGHBORHOOD, RACE/ETHNICITY')
plt.ylabel('AGE')
plt.show()
