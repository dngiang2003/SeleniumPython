from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://dongocgiang.click/thuchanh/coban.html")

# Điền "Nội dung" vào ô input có ID là "input"
sleep(2)
driver.find_element(By.ID, "input").send_keys("Nội dung")

# Click vào phần tử có ID là "btnAlert"
sleep(2)
driver.find_element(By.ID, "btnAlert").click()

# Lấy text của phần tử có ID là "result"
sleep(2)
result = driver.find_element(By.ID, "result").text
print(result)

# Lấy giá trị của thuộc tính trong thẻ p
sleep(2)
p = driver.find_element(By.TAG_NAME, "p")
value = p.get_attribute("style")
print(value)

# Đóng Chrome
sleep(3)
driver.quit()










