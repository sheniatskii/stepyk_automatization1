from selenium import webdriver
import time,math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    input_1 = browser.find_element_by_id("answer").send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    click_1 =  browser.find_element_by_class_name("form-check-input").click()
    click_2  = browser.find_element_by_id("robotsRule").click()
    button.click()
    # Отправляем заполненную форму
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
