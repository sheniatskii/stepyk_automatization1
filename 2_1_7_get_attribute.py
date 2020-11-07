from selenium import webdriver
import time,math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    treasure_element = browser.find_element_by_id("treasure")
    x = treasure_element.get_attribute("valuex")
    y = calc(x)
    input_1 = browser.find_element_by_id("answer").send_keys(y)
    click_1 =  browser.find_element_by_id("robotCheckbox").click()
    click_2  = browser.find_element_by_id("robotsRule").click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
