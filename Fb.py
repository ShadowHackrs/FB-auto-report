banner = '''
░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░  
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗  
╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝  ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝  
░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░  ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  
██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║  
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  

███████╗██████╗░  ░█████╗░██╗░░░██╗████████╗░█████╗░  ██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
██╔════╝██╔══██╗  ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
█████╗░░██████╦╝  ███████║██║░░░██║░░░██║░░░██║░░██║  ██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
██╔══╝░░██╔══██╗  ██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║░░░░░██████╦╝  ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝░░░░░╚═════╝░  ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
'''

print(banner)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Prompt the user for email and password
email = input("Enter your email or phone number: ")
password = input("Enter your password: ")

# Prompt the user for the account URL and number of reports
account_url = input("Enter the account URL you want to report: ")
report_count = int(input("Enter the number of reports you want to send: "))

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")

time.sleep(4)
driver.find_element_by_id("email").send_keys(email)
time.sleep(2)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()
time.sleep(4)
driver.get(account_url)

time.sleep(4)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]').click()  # three dots
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]').click()  # find or report
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # report option
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # me
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[4]/div/div').click()  # submit
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div').click()  # next button
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div/div').click()  # done
time.sleep(30)

for i in range(report_count - 1):
    driver.get(account_url)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]').click()  # three dots
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]').click()  # find or report
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # report option
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # me
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[4]/div/div').click()  # submit
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div').click()  # next button
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div/div').click()  # done
    time.sleep(30)

driver.quit()
