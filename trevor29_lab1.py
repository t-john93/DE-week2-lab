import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns
import re
from IPython.display import display
# %matplotlib inline

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
# type(soup)
# title = soup.title
# print(title)

# text = soup.text

# anchors = soup.find_all('a')

# for anchor in anchors:
#     print(anchor.get('href'))

rows = soup.find_all('tr')
# print(rows[:10])

# for row in rows:
#     row_td = row.find_all('td')
#     str_cells = str(row_td)
#     cleantext = BeautifulSoup(str_cells, "lxml").get_text()
#     print(cleantext)
# print(row_td)
# type(row_td)


list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
    # print(clean2)
    # type(clean2)

df = pd.DataFrame(list_rows)
df.head(10)
df1 = df[0].str.split(',', expand=True)
display(df1.head(10))
col_labels = soup.find_all('th')