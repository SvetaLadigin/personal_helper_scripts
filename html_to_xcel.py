from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
import os

# simple module to dump all products and prices to excel / csv using selenium and BeautifulSoup


usr = os.getlogin()
# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('C:\\Users\\'+usr+'\\Desktop\\scrapper.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'names', bold)
worksheet.write('B1', 'prices', bold)

# open chrome without window to search

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('C:\\Users\\'+usr+'\\Downloads\\chromedriver_win32\\chromedriver.exe', options=option)
url = 'https://shulinka.co.il/' # some url

products=[] # List to store name of the product
prices=[] # List to store price of the product
column_list = [] # List to store links of the page

driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# find the links to the categories

for link in soup.findAll('a'):
    link_name =link.get('href')
    if('https://shulinka.co.il/product-category/' in link_name ):
        column_list.append(link.get('href'))
        print(link.get('href'))

i = 0
j = 0
# start searching for names and prices in the links

for link in column_list:
    driver = webdriver.Chrome('C:\\Users\\'+usr+'\\Downloads\\chromedriver_win32\\chromedriver.exe', options=option)
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    for name in soup.findAll('h2', attrs={'class':'woocommerce-loop-product__title'}):
        print(name.text)
        products.append(name.text)
        price = name.findNextSibling().text
        print(price)
        prices.append(price)
        worksheet.write(i, 1, price)
        worksheet.write(i, 0, name.text)
        i = i+1
    driver.close()

# optional create data frame in pandas - problems in hebrew
df = pd.DataFrame({'Product Name': products, 'Price': prices})
print(df)
df.to_csv('products.csv', index=False, encoding='utf-8')

driver.quit()
workbook.close()


