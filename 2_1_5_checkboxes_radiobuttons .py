from selenium import webdriver
import time,math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector(".form-group .nowrap:nth-child(2)")
    x = x_element.text
    y = calc(x)
    input_1 = browser.find_element_by_id("answer").send_keys(y)
    click_1 =  browser.find_element_by_class_name("form-check-input").click()
    click_2  = browser.find_element_by_id("robotsRule").click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
