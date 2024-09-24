"""
Author: 刘宇航
Created: 2023-12-18
Version: 1.0
License: MIT License

"""

import subprocess
import time
import os
from Viewtickets import Redfor

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 账号信息列表，每个字典包含用户名、密码和登录URL
accounts = [
    {"username": "mima1", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "zxoz", "password": "Eoms123", "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    #密码错误{"username": "silangdouji", "password": "Eoms123", "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "dwcrsnsc", "password": "Eoms123", "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "crzx3", "password": "Eoms123", "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "luobu1", "password": "Eoms123", "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "zwn_jmqd", "password": "Eoms123", "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "qiangbasangzhu", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "sldz1", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "cirensangzhu", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "crnm", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "nimajiacuo", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "qiongdej", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    #{"username": "liudailun", "password": "13989938986",
    #"url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "dongyue", "password": "15708035484",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "zhaxiduobujie", "password": "13989036945",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "tanghaokai", "password": "13908935723",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "panfaui", "password": "17867632121",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "luobuciren", "password": "Emos123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "luodan", "password": "18289079123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "qiangbaozhu", "password": "19889135155",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "awangjina", "password": "13889038912",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "bazhu", "password": "13908937787",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "zhaxibazhu", "password": "13658935535",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "nimaduoji", "password": "18308030600",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "danzeng", "password": "13908936991",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "zhadun", "password": "13648935023",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "tajiciren", "password": "18389032299",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "yundansangbu", "password": "1526739299",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "caojun", "password": "17888039578",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "wangwei", "password": "13989939719",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "cirensangzhu", "password": "18308036633",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "zhaopan", "password": "Eoms123",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "cirendouji", "password": "18289136000",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "gama", "password": "14718903956",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "zhaxidajie", "password": "18289132533",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "bianbadunzhu", "password": "18798932195",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "litao", "password": "18798930946",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "luqiang", "password": "14728930054",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "gesangdajie", "password": "18308038320",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"},
    {"username": "shannanjifang", "password": "13908935564",
     "url": "http://10.241.124.126:30080/frame/login?redirect=http%3A%2F%2F10.241.124.126%3A30080%2Fhome"}

    # 添加更多账号信息...
]

# 创建Selenium WebDriver实例
driver = webdriver.Chrome()
redfor = Redfor()

# 循环处理每个账号的登录和相关操作
for account in accounts:
    # 打开登录页面
    driver.get(account["url"])

    # 等待页面加载完成
    # wait = WebDriverWait(driver, 20)

    # 定位到用户名输入框并输入用户名
    # 使用XPath表达式定位到具有特定属性的<input>元素
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//html//body//div//div//div[2]//div[2]//form//div[1]//div//div//div//div//input")))
    # = driver.find_element(By.XPATH,"//html//body//div//div//div[2]//div[2]//form//div[1]//div//div//div//div//input")
    username_input.click()  # 点击输入框
    username_input.send_keys(account["username"])

    # 定位到密码输入框并输入密码
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/input")))
    password_input.click()  # 点击输入框
    password_input.send_keys(account["password"])

    # 定位到登录按钮并点击
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//html//body//div//div//div[2]//div[2]//form//div[3]//div//div//div//button")))
    login_button.click()
    time.sleep(20)


    # 下面为账号内业务操作
    count = 0  # 计数器，记录连续出现 "-" 的次数
    def find_work_order(driver, wait_time):
        while True:
            xpath_list = [
                "/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/span",
                "/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[6]/span",
                "/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[6]/span",
                "/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[4]/td[6]/span",
                "/html/body/div[1]/div/section/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[5]/td[6]/span"
            ]

            for xpath in xpath_list:
                try:
                    time_element = None
                    time_element = WebDriverWait(driver, wait_time).until(
                        EC.presence_of_element_located((By.XPATH, xpath)))
                    time_text = time_element.text
                    if time_text != "-" and time_text is not None:
                        work_order_number_element = WebDriverWait(driver, wait_time).until(
                            EC.presence_of_element_located((By.XPATH, xpath.replace("/td[6]/span", "/td[1]/span"))))
                        number_text = work_order_number_element.text
                        print("工单号为：", number_text)
                        work_order_number_element.click()
                        print("已点击工单号")
                        time.sleep(10)
                        redfor.set_alert_title(driver)
                        # subprocess.run(["python", "Viewtickets.py"])
                        time.sleep(10)
                    else:
                        print("没有工单")
                        break
                except (NoSuchElementException, TimeoutException):
                    continue

            # 没有找到合适的工单或者没有更多工单，跳出循环
            break


    wait_time = 10  # 等待时间
    find_work_order(driver, wait_time)

    # 关闭浏览器
driver.quit()
