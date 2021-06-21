#  From selenium library, imported webdriver
from selenium import webdriver

# Imported By
from selenium.webdriver.common.by import By

# Imported WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

# Imported Expected Condition as EC
from selenium.webdriver.support import expected_conditions as EC

# Here we set 'gecodriver.exe' path in '   '
driver = webdriver.Firefox(executable_path=r'C:\Users\saurabh\Documents\gecodriver\geckodriver.exe')

# Here we set web-site url in "  "
driver.get("https://www.google.com/")

# Here you can set your required 'expected condition ' & also your ' Elements' By.(XPATH, ID, TAGNAME, etc...)
# Also you can change waiting time period : (driver,'Your required wait time' )
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]"))
    )
finally:

# Here we close our browser using .quit() method
    driver.quit()
