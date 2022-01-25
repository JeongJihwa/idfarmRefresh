# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json


if __name__ == "__main__":
    print("아이디팜 갱신 시작!")
    with open('/src/info.json') as info_file:
        information = json.load(info_file)
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")

    chDriverPath = '/usr/bin/chromedriver'
    try:
        pipdriver = webdriver.Chrome(chDriverPath, chrome_options=options)
        pipdriver.get("https://idfarm.co.kr/bbs/login.php")
        pipdriver.implicitly_wait(10)
        pipdriver.find_element(By.NAME, 'mb_id').send_keys(information['id'])
        pipdriver.find_element(By.NAME, 'mb_password').send_keys(information['pw'])
        pipdriver.find_element(By.XPATH, '//*[@id="login_fs"]/button').click()
        pipdriver.implicitly_wait(10)
        pipdriver.get("https://idfarm.co.kr/trade.php?mode=1")
        pipdriver.implicitly_wait(10)
        try:
            i = 2
            while True:
                pipdriver.find_element(By.CSS_SELECTOR, f'#sblistWrap > div:nth-child({i}) > div.sbWrapset > div.pcsbWrapset > div.itemRewrite').click()
                sleep(0.7)
                pipdriver.switch_to.alert.accept()
                try:
                    sleep(0.7)
                    pipdriver.switch_to.alert.accept()
                except:
                    pass
                sleep(60)
                i += 1
        finally:
            pass

    except Exception as e:
        print(e)

    pipdriver.quit()