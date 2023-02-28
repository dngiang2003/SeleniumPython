from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://eop.edu.vn")

# Tiến hành điền mã sinh viên
sleep(2)
maSinhVien = "2021603812"
driver.find_element(By.XPATH, '//*[@id="kehoachhoctap"]/div/div[1]/div[1]/input').send_keys(maSinhVien)

# Ấn vào nút "Tra cứu" để gửi yêu cầu lên server
sleep(2)
driver.find_element(By.XPATH, '//*[@id="kehoachhoctap"]/div/div[1]/div[2]/button').click()

# Tiến hành lấy ra tên sinh viên
sleep(2)
tenSinhVien = driver.find_element(By.XPATH, '//*[@id="kehoachhoctap"]/div/div[3]/h4/b').text
print(tenSinhVien) 
# Lê Thu Phương

# Đóng Chrome
sleep(3)
driver.quit()










