from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Mở Chrome
driver = webdriver.Chrome()

# Đi đến trang web test
sleep(1)
driver.get("https://dongocgiang.click/thuchanh/alert.html")

# Nhấn nút gây ra alert
sleep(1)
driver.find_element(By.ID, "/html/body/button").click()

# Chuyển sang alert
sleep(1)
alert = driver.switch_to.alert

# Lấy nội dung của alert và in ra
sleep(1)
print(alert.text) # Chọn 1 trong 2 :))

# Chấp nhận alert
sleep(1)
alert.accept()

# Hoặc hủy bỏ alert
# alert.dismiss()

# Đóng trình duyệt
driver.quit()