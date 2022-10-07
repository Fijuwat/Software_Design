from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.common.alert import Alert
from datetime import datetime
from selenium.webdriver.chrome.options import Options

res = []
data = pd.read_csv("C:/Users/wawu/Downloads/Current List of Licensed Office Users.csv", encoding= 'unicode_escape')
name_list = data['Display name']
test_list = name_list[0:15]




def web_scrape(names):

    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )

    driver = webdriver.Chrome(chrome_options=option, executable_path=r"C:/Users/wawu/Downloads/chromedriver_win32 (1)/chromedriver")
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    driver.get("https://silabs.service-now.com/nav_to.do?uri=%2F$pa_dashboard.do")
    username = driver.find_element(By.ID, "okta-signin-username")
    password = driver.find_element(By.ID, "okta-signin-password")
    username.send_keys("wawu")
    password.send_keys("!QAZ@WSX3edc")
    # Step 4) Click Login
    submit = driver.find_element(By.ID, "okta-signin-submit")
    submit.click()
    time.sleep(5)
    for name in names:
        time.sleep(10000)
        search = driver.find_element(By.ID, "sysparm_search")
        search.send_keys(name)
        search.send_keys(Keys.RETURN)
        driver.switch_to.frame("gsft_main")
        #terminate = driver.find_elements(By.CLASS_NAME, "linked")

        wait = WebDriverWait(driver, 10)

        try:
            terminate = [element.text for element in
                      wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "linked")))]
            for text in terminate:
                if text.startswith('Terminate Access'):
                    res.append([name, True])
                    driver.switch_to.default_content()
                    search.clear()
                    break
                else:
                    if terminate[len(terminate)-1] == text:
                        res.append([name, False])
                        driver.switch_to.default_content()
                        search.clear()
                        break


        except:
            res.append("No factor to determine")
            driver.switch_to.default_content()
            search.clear()




    return res



df = pd.DataFrame(web_scrape(test_list), columns=["name","Should_be_block"])
df.to_csv(r'C:/Users/wawu/Desktop/Access/access.csv', index=True, encoding='utf-8')