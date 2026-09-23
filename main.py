from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def passing_values():

    driver = webdriver.Chrome()

    driver.get("http://localhost:8000/login.html")

    for count in range(10000):

        number = f"{count:04d}"

        password_box = driver.find_element(By.ID, "password")

        password_box.clear()
        password_box.send_keys(number)

        driver.find_element(By.ID, "login").click()

        result = driver.find_element(By.ID, "result").text

        print(number, result)

        if result == "Correct password!":
            print("Found:", number)
            break

    time.sleep(5)
    driver.quit()


passing_values()