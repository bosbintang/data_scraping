# importing necessary package
import requests
from bs4 import BeautifulSoup
import pandas as pd


# reading webpage
def active_stock():
    try:
        page = requests.get('https://finance.yahoo.com/most-active')
    except Exception:
        return None
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')

        # reading table
        table = soup.find('table', {'class': 'W(100%)'})

        # creating table
        header = []
        for i in table.find_all('th'):
            title = i.text
            header.append(title)

        mydata = pd.DataFrame(columns=header)
        for j in table.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            length = len(mydata)
            mydata.loc[length] = row

        print(mydata)
