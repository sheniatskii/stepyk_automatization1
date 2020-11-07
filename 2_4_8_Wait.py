from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()



    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input_1 = browser.find_element_by_id("answer").send_keys(y)
    # Отправляем заполненную форму
    button1 = browser.find_element_by_id("solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
