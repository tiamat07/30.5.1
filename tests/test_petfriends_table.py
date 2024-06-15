import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(auth_pets): #Проверка, что на странице с моими животными, все питомцы с разными именами
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pet_data = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   r = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         r += 1
   assert r == 0

def test_no_duplicate_pets(auth_pets): #Прорверка, что на странице с моими животными нет повторяющихся животных
   driver = auth_pets

   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr"))) # Устанавливаем явное ожидание

   pet_data = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   list_data = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      list_data.append(split_data_pet)

   line = '' #Соеденяем имя+возраст+порода. Результат бодовляем в строку с добовлением пробела м/у ними
   for i in list_data:
      line += ''.join(i)
      line += ' '

   list_line = line.split(' ')#Список из строки line
   set_list_line = set(list_line)#делаем из списка множество
   result = len(list_line) - len(set_list_line)# Из количества элементов списка вычитаем количество элементов множества
   assert result == 0 # Если количество элементов == 0,то карточки с одинаковыми данными отсутствуют

def test_photo_availability(auth_pets):#Прорверка, что на странице с моими животными хотя бы у половины питомцев есть фото
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   statistic = driver.find_elements(By.CSS_SELECTOR,".\\.col-sm-4.left")
   images = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover img')

   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   half = number // 2# получаем половину от количества питомцев

   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1# Получаем количество питомцев с фотографией

   assert number_а_photos >= half# Проверка на то,что количество питомцев с фотографией больше или равно половине количества питомцев