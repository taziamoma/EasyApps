from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_path = "C:/Users/Taziamoma/iCloudDrive/Documents/Taz Personal/Programming/Coding/Python/BasicApps/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get("https://www.iqcent.com/en/login")
delay = 0


try:
    email_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'form-input ng-valid-email")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


email_box = driver.find_element_by_xpath("//input[contains(@class,'form-input ng-valid-email')]")
#pass_box = driver.find_element_by_class_name('form-input ng-pristine ng-empty ng-invalid ng-in//input[contains(@class,'form-input ng-valid-emailvalid-required ng-touched')
#login_button = driver.find_element_by_class_name('button ui iq fluid huge')

email_box.send_keys('taziamoma@gmail.com')