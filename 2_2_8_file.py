from selenium import webdriver
import time,math, os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element_by_name("firstname").send_keys("SS")
    input_2 = browser.find_element_by_name("lastname").send_keys("SS")
    input_3 = browser.find_element_by_name("email").send_keys("SS")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    file =  browser.find_element_by_id("file").send_keys(file_path)
    time.sleep(1)
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    # Отправляем заполненную форму
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
