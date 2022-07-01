from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from faker import Faker
import time
import secrets
import string
import base64
import cv2
from io import BytesIO
from PIL import Image
import os
import numpy as np

#Settings
while True:
    faker = Faker()
    options = Options()
    profile = webdriver.FirefoxProfile() 
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9050)
    full_name = faker.name().split()
    driver = webdriver.Firefox(executable_path=r"/mnt/storage/nvme/Python-Code/personal/captcha/geckodriver", options=options, firefox_profile=profile)
    driver.get("https://www.twilio.com/try-twilio")
    while True:
        try:
            if driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div"):
                driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys(full_name[0])
                driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys(full_name[1])
                driver.find_element(By.XPATH, '//*[@id="EmailAddr"]').send_keys("{}.{}@{}".format(full_name[0], full_name[1], faker.domain_name()))
                driver.find_element(By.XPATH, '//*[@id="Passwd"]').send_keys(str(''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(16))))
                driver.find_element(By.XPATH, '//*[@id="Tos"]').click()
                time.sleep(5)
                driver.find_element(By.XPATH, '//*[@id="signup-button"]').click()
                break
        except:
            pass
    print("Next Stage")
    while True:
        try:
            driver.switch_to.default_content()
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[3]/iframe"))
            driver.switch_to.frame("fc-iframe-wrap")
            driver.switch_to.frame("CaptchaFrame")
            driver.find_element(By.XPATH, '//*[@id="home_children_button"]').click()
            time.sleep(5)
            base64_image = driver.find_element_by_xpath('//*[@id="game_challengeItem_image"]').get_attribute("src")
            #print(base64_image)
            with open("/mnt/storage/nvme/Python-Code/personal/captcha/base64.txt", "w+") as base64_text:
                base64_text.write(base64_image.replace("data:application/octet-stream;base64,", ""))
                break
        except:
            pass

    def crack():
        start_time = time.time()
        f = open('/mnt/storage/nvme/Python-Code/personal/captcha/base64.txt', 'r')
        data = f.read()
        f.closed
        im = Image.open(BytesIO(base64.b64decode(data)))
        im.save('/mnt/storage/nvme/Python-Code/personal/captcha/current_captcha.png', 'PNG')
        
        width, height = im.size
        top_image_1_left = 10.00
        top_image_1_top = 10.00
        top_image_1_right = 90
        top_image_1_bottom = 90
        im1 = im.crop((top_image_1_left, top_image_1_top, top_image_1_right, top_image_1_bottom))
        im1.save("/mnt/storage/nvme/Python-Code/personal/captured_stars/1.png")

        top_image_2_left = 110
        top_image_2_top = 10.00
        top_image_2_right = 190
        top_image_2_bottom = 90
        im1 = im.crop((top_image_2_left, top_image_2_top, top_image_2_right, top_image_2_bottom))
        im1.save("/mnt/storage/nvme/Python-Code/personal/captured_stars/2.png")

        top_image_3_left = 210
        top_image_3_top = 10.00
        top_image_3_right = 290
        top_image_3_bottom = 90
        im1 = im.crop((top_image_3_left, top_image_3_top, top_image_3_right, top_image_3_bottom))
        im1.save("/mnt/storage/nvme/Python-Code/personal/captured_stars/3.png")

        bottom_image_1_left = 10.00
        bottom_image_1_top = 110
        bottom_image_1_right = 90
        bottom_image_1_bottom = 190
        im1 = im.crop((bottom_image_1_left, bottom_image_1_top, bottom_image_1_right, bottom_image_1_bottom))
        im1.save("/mnt/storage/nvme/Python-Code/personal/captured_stars/4.png")

        bottom_image_2_left = 110
        bottom_image_2_top = 110
        bottom_image_2_right = 190
        bottom_image_2_bottom = 190
        im1 = im.crop((bottom_image_2_left, bottom_image_2_top, bottom_image_2_right, bottom_image_2_bottom))
        im1.save("/mnt/storage/nvme/Python-Code/personal/captured_stars/5.png")

        bottom_image_3_left = 210
        bottom_image_3_top = 110
        bottom_image_3_right = 290
        bottom_image_3_bottom = 190
        im1 = im.crop((bottom_image_3_left, bottom_image_3_top, bottom_image_3_right, bottom_image_3_bottom))
        im1.save("/mnt/storage/nvme/Python-Code/personal/captured_stars/6.png")
        ####
        total = {
            "1.png": [],
            "2.png": [],
            "3.png": [],
            "4.png": [],
            "5.png": [],
            "6.png": [],
            }

        for x in os.listdir("/mnt/storage/nvme/Python-Code/personal/captured_stars/"):
            found = 0
            img = cv2.imread("/mnt/storage/nvme/Python-Code/personal/captured_stars/"  + str(x))
            hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            for check in os.listdir("/mnt/storage/nvme/Python-Code/personal/more_success/"):
                template_temp = cv2.imread("/mnt/storage/nvme/Python-Code/personal/more_success/" + str(check))
                hsv_image_temp = cv2.cvtColor(template_temp,cv2.COLOR_BGR2HSV)
                result = cv2.matchTemplate(hsv_image, hsv_image_temp, cv2.TM_CCORR_NORMED)
                for pt in zip(*result[::-1]):
                    found += pt[0]
            add = []
            add.append(found)
            a = sum(add)
            total[x].append(a)
        pick = max(total, key=total.get)
        print(total)
        print(pick)
        print("--- %s seconds ---" % (time.time() - start_time))
        picture_count = len(os.listdir("/mnt/storage/nvme/Python-Code/personal/more_success/")) + 1
        os.rename("/mnt/storage/nvme/Python-Code/personal/captured_stars/" + str(pick), "/mnt/storage/nvme/Python-Code/personal/more_success/" + str(picture_count) + ".png")
        if pick == "1.png":
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/div/ul/li[1]/a").click()
            print("Picked image 1")
        if pick == "2.png":
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/div/ul/li[2]/a").click()
            print("Picked image 2")
        if pick == "3.png":
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/div/ul/li[3]/a").click()
            print("Picked image 3")
        if pick == "4.png":
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/div/ul/li[4]/a").click()
            print("Picked image 4")
        if pick == "5.png":
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/div/ul/li[5]/a").click()
            print("Picked image 5")
        if pick == "6.png":
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/div/ul/li[6]/a").click()
            print("Picked image 6")
        time.sleep(5)
    while True:
        try:
            if driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[1]/h2").get_attribute("innerHTML") == "Pick the spiral galaxy":
                base64_image = driver.find_element_by_xpath('//*[@id="game_challengeItem_image"]').get_attribute("src")
                with open("/mnt/storage/nvme/Python-Code/personal/captcha/base64.txt", "w+") as base64_text:
                    base64_text.write(base64_image.replace("data:application/octet-stream;base64,", ""))
                crack()
            if driver.find_element(By.XPATH, '//*[@id="wrong_children_exclamation_text"]').get_attribute("innerHTML") == "Whoops! That's not quite right.":
                driver.quit()
                break
        except:
            pass
    print("Stoppped")