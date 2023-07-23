from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeService
import time

# Set the path to the Microsoft Edge Driver executable
edge_driver_path = "E:\Dev Tools\Python\Selenium\edgedriver_win64\msedgedriver.exe"

# Create an instance of the EdgeOptions class
options = EdgeOptions()

# Set the accept_insecure_certs option to True
options.accept_insecure_certs = True
options.add_argument('--ignore-certificate-errors')

# Create an instance of the EdgeService class with the executable path
service = EdgeService(executable_path=edge_driver_path)

# Create an instance of the Edge driver with the options and service
driver = Edge(service=service, options=options)

driver.get('http://192.168.1.250/admin')

# Find the username and password fields and enter the login credentials
username_field = driver.find_element(By.ID, 'ext-gen46')
password_field = driver.find_element(By.ID, 'ext-gen48')
username_field.send_keys('admin')
password_field.send_keys('')

# Click the login button
login_button = driver.find_element(By.CLASS_NAME, 'fe_Login_btn')
login_button.click()

time.sleep(2)

# Click AntiSpam button
antispam_button = driver.find_element(By.ID, 'ext-gen506')
antispam_button.click()

time.sleep(1)

# Click Block/Safe List button
blocksafe_button = driver.find_element(By.ID, 'gwt-uid-41')
blocksafe_button.click()

time.sleep(1)

# Click Block List button
blocklist_button = driver.find_element(By.ID, 'blocklist')
blocklist_button.click()

time.sleep(1)

# Add mail address to block list
input_field = driver.find_element(By.ID, "ext-gen2000")
input_field.send_keys('test1@tmail.com')

time.sleep(1)

# Click Add button
add_button = driver.find_element(By.CLASS_NAME, 'x-btn-text')
add_button.click()

time.sleep(1)


# Click Add button
add_button = driver.find_element(By.LINK_TEXT, 'Add')
add_button.click()

time.sleep(5)

driver.quit()