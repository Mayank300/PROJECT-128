from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import datetime

URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

temp_list= []
Star_names = []
Distance =[]
Mass = []
Radius =[]


web_page = requests.get(URL)
print(web_page)

time_stamp = datetime.datetime.now().strftime('%H-%M-%S')
file_name = f'{time_stamp}.csv'

soup = bs(web_page.text,'html.parser')
star_table = soup.find('table')
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv(file_name)