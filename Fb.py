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

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")

time.sleep(4)
driver.find_element_by_id("email").send_keys('You Email in facebook') #replace with your email or phone  number
time.sleep(2)
driver.find_element_by_id("pass").send_keys('You Password account') #replace with your password
time.sleep(2)
driver.find_element_by_name("login").click()
time.sleep(4)

account_url = 'https://www.facebook.com/xxxxxxxxxxxx'  # replace with the account URL you want to report
report_count = 0  # the number of reports you want to send

while True:
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
    
    report_count += 1
    print("Report count:", report_count)

    if report_count >= 100:  # Modify this condition as per your requirements
        break

driver.quit()
