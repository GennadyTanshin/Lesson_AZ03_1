import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import pandas as pd
import matplotlib.pyplot as plt

geckodriver_path = 'C:\\Geckodriver\\geckodriver.exe'
firefox_binary_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

service = Service(geckodriver_path)
options = Options()
options.binary_location = firefox_binary_path

driver = webdriver.Firefox(service=service, options=options)
driver.get('https://www.divan.ru/category/divany-i-kresla')

time.sleep(5)

sofa_prices = []

divans = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
for divan in divans:
    try:
        price = divan.find_element(By.CSS_SELECTOR, 'div.q5Uds span').text
        price = price.replace(' ', '')  # Убираем пробелы в строке
        price = int(price[:-4])  # Преобразуем в целое число

    except Exception as e:
        print(f"Произошла ошибка при парсинге{e}")
        continue
    sofa_prices.append(price)

driver.quit()

# Сохранение данных в CSV файл
csv_file = 'sofa_prices.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])
    for price in sofa_prices:
        writer.writerow([price])

# Чтение данных из CSV файла
df = pd.read_csv(csv_file)

# Вычисление средней цены
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} руб.')

# Построение гистограммы цен на диваны
plt.hist(df['Price'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.show()
