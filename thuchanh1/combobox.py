from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from random import randint
from time import sleep


driver = webdriver.Chrome()
driver.get("https://dongocgiang.click/thuchanh/combobox.html")

# ---- Đoạn này cách 1 tôi demo chọn ngày ---- #
# Tìm đến combobox
sleep(1)
combobox = driver.find_element(By.ID, "day")

# Tạo đối tượng Select từ combobox
select = Select(combobox)

# Chọn giá trị trong combobox bằng giá trị của option
# sleep(1)
# select.select_by_value("1")

# Hoặc chọn giá trị trong combobox bằng văn bản của option
# sleep(1)
# select.select_by_visible_text("2")

# 2 cách trên khi biết trước text hoặc giá trị
# Hoặc chọn giá trị trong combobox bằng số thứ tự của option (bắt đầu từ 0)
sleep(1)
select.select_by_index(2)

# ---- Còn đoạn này cách 2 tôi demo chọn tháng ---- #
# ---- Cách này do tôi tự mò trong quá trình làm --- #

# Click vào ô select cho nó hiển thị ra các giá trị
sleep(1)
driver.find_element(By.ID, "month").click()

# Click ngẫu nhiên hoặc mình tự set giá trị mong muốn
# thông qua chỉ số ở XPATH
# //*[@id="month"]/option[1] đây là giá trị đầu tiên [1]
# ......
# //*[@id="month"]/option[12] đây là giá trị cuối [12]
sleep(1)
driver.find_element(By.XPATH, f'//*[@id="month"]/option[{randint(1, 12)}]').click()

# Click btn hiển thị kết quả
sleep(1)
driver.find_element(By.ID, "btn-submit").click()

# Đóng trình duyệt
sleep(10)
driver.quit()