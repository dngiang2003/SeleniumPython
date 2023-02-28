from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Mở Chrome
driver = webdriver.Chrome()

# Đến trang test
sleep(1)
driver.get("https://dongocgiang.click/thuchanh/prompt.html")

# Nhấn nút gây ra Prompt
sleep(1)
driver.find_element(By.ID, "btn-submit").click()

# Chuyển sang Prompt
sleep(1)
prompt = driver.switch_to.alert

# Nhập giá trị vào Prompt và chấp nhận Prompt
sleep(1)
prompt.send_keys("Hello, World!")
sleep(1)
prompt.accept()

# Hoặc hủy bỏ Prompt
# prompt.dismiss()

# Đóng trình duyệt
sleep(1)
driver.quit()