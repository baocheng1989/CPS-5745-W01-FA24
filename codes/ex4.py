
#Extracting the number of COVID cases.
import requests
from bs4 import BeautifulSoup

import pandas as pd

# for Visualizatin
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import rcParams
from matplotlib.pyplot import figure

import texttable as tt

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

# Scrape everything
data_iterator = iter(soup.find_all('td'))
# Using loop
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text
        data.append((
        country,
        (confirmed.replace(', ', '')),
        (deaths.replace(',', '')),
        continent
        ))
    except StopIteration:
       break

data.sort(key = lambda row: row[1], reverse = True)

df = pd.DataFrame(data,columns=['country','Number of cases','Deaths','Continent'])
#print(df.head())
df['Number of cases'] = [x.replace(',', '') for x in df['Number of cases']]
df['Number of cases'] = pd.to_numeric(df['Number of cases'])
#
#print(df)
#
# # to get Info
#print(df.info())
#
# #Create Death_rate Column
dff = df.sort_values(by ='Number of cases',ascending = False)
t = dff['Deaths'].astype(float)
t1 = dff['Number of cases'].astype(float)
dff['Death_rate'] = (t / t1)*100
print(dff.head())
#
#
# # Plotting
rcParams['figure.figsize'] = 15, 10
sns.pairplot(dff,hue='Continent')
plt.show()
#
# Bar plot
figure(num=None, figsize=(20, 6), dpi=80, facecolor='w', edgecolor='k')
sns.barplot(hue='Continent', x = 'country',y = 'Number of cases',data = dff.head(10), palette='Set2')

plt.show()

sns.scatterplot(x = "Number of cases", y = "Deaths",hue = "Continent",data = dff.head(10))
plt.show()

# Group and Sort the Data
#SeriesGroupBy.sum


dfg = dff.groupby(by = 'Continent',as_index = False).agg({'Number of cases':sum,'Deaths':sum})
dfgg = dfg[1:]
df1 = dfgg.sort_values(by = 'Number of cases',ascending = False)

df1['Death_rate'] = (df1['Deaths'].astype(float) /df1['Number of cases'])*100
df1.sort_values(by = 'Death_rate',ascending = False)

print(df1)
sns.barplot(hue='Continent', x = 'Continent',y = 'Death_rate',data = df1.sort_values(by = 'Death_rate',ascending = False), palette='Set2')
plt.show()

table = tt.Texttable()

table.add_rows([(None, None, None, None)] + data)
table.set_cols_align(('c', 'c', 'c', 'c'))  # 'l' denotes left, 'c' denotes center, and 'r' denotes right
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))

print(table.draw())