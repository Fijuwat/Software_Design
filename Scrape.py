from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.common.alert import Alert
from datetime import datetime
from selenium.webdriver.chrome.options import Options

res = []
data = pd.read_csv(r"C:\Users\Austin\Downloads\Fraud_vs_non-fraud.csv", encoding= 'unicode_escape')
link_list = data['FB Link']
str1 = "https://"
loc = []

def web_scrape(links):
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )

    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)


    driver.get("http://www.facebook.com")
    username = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    submit = driver.find_element(By.CLASS_NAME, "_6ltg")
    username.send_keys("jjlin12313@gmail.com")
    password.send_keys("!QAZ@WSX3edc")
    # Step 4) Click Login
    submit.click()
    
    print(f'len(links) = {len(links)}')
    for link in links:
        time.sleep(0.2)
        driver.get(str1 + link)
        lst_about = driver.find_elements(By.CLASS_NAME, "gvxzyvdx.aeinzg81.t7p7dqev.gh25dzvf.exr7barw.b6ax4al1.gem102v4.ncib64c9.mrvwc6qr.sx8pxkcf.f597kf1v.cpcgwwas.m2nijcs8.hxfwr5lz.k1z55t6l.oog5qr5w.tes86rjd.pbevjfx6.ztn2w49o")
        el = [x.text[9:] for x in lst_about if x.text.startswith("Lives in")]
        if len(el) > 0:
            loc.append(el[0])
        else:
            loc.append('')
    return loc



df = pd.DataFrame(web_scrape(link_list), columns=["location"])
df.to_csv(r"C:\Users\Austin\Downloads\Demo.csv", index=True, encoding='utf-8')
