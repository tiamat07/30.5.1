import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_show_pet_friends(auth_pets):#Проверка карточек питомцев
   driver = auth_pets
   driver.implicitly_wait(10)# Установка неявного ожидание

   assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'# Проверка, что мы находимся на главной странице пользователя


def test_there_is_a_name_age_and_gender(auth_pets):#Прорверка, что на странице с моими животными, у всех питомцев есть имена,возраст и порода
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pet_data = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   for i in range(len(pet_data)):  #Перебираем данные из pet_data
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '') #оставляем имя, возраст, и породу остальное меняем на пустую строку
      split_data_pet = data_pet.split(' ')  #разделяем по пробелу
      result = len(split_data_pet)  #Находим количество элементов в получившемся списке
      assert result == 3  #сравниваем их с ожидаемым результатом

def test_all_pets_are_present(auth_pets): #Прорверка, что на странице с моими животными, присутствуют все питомцы
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pets = driver.find_element(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1]) # Получаем количество питомцев из данных статистики

   number_of_pets = len(pets)  # количество карточек питомцев

   assert number == number_of_pets # Проверяем что количество питомцев совпадает с количеством карточек питомцев