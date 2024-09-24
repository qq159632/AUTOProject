"""
Author: 刘宇航
Created: 2023-12-18
Version: 1.0
License: MIT License
#  Viewtickets.py
"""
import re
import subprocess

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from OLTtuifu import WorkOrder as OLTWorkOrder
from Transmission_blackout import WorkOrder as TransmissionWorkOrder
from bankayichang import WorkOrder as BankayiWorkOrder
from chuansongwang import WorkOrder as chuansongwangWorkOrder
from guangmokuaiyichang import WorkOrder as GuangmokuaiWorkOrder


# 导入 autofile 和 webdriver 模块



class Redfor:
    def set_alert_title(self, driver):
        # workorder = WorkOrder()
        # 获取告警标题
        alert_title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[1]/div[2]/div/div/form/div[2]/div/div/div[2]/div/div/div")))
        alert_title = alert_title_element.text
        print("告警标题：", alert_title)

        # 定义问题匹配的模式
        # 断纤
        pattern_duanqian = r"断纤"
        # 板卡异常
        pattern_bankayichang = r"板卡异常"
        # 传光模块异常
        pattern_guangmokuaiyichang = r"光模块异常"
        # 传送网
        pattern_chuansongwang = r"传送网"
        # 集客
        pattern_jike = r"集客"
        # 话音网
        pattern_huayinwang= r"话音网"
        # 话音网|动环原因
        pattern_donghuanyuanyin= r"话音网|动环原因"
        # 动力环境
        pattern_donglihuanjing = r"动力环境"
        # OLT退服
        pattern_OLTtuifu = r"OLT退服"
        # 数据网
        pattern_shujuwang = r"数据网"
        # 进行模式匹配
        transmission_blackout = re.search(pattern_duanqian, alert_title)
        power_outage_on_the_user_side = re.search(pattern_bankayichang, alert_title)
        single_board_dislocation = re.search(pattern_guangmokuaiyichang, alert_title)
        transmission_chuansongwang = re.search(pattern_chuansongwang, alert_title)
        transmission_jike = re.search(pattern_jike, alert_title)
        transmission_huayinwang = re.search(pattern_huayinwang, alert_title)
        transmission_donghuanyuanyin = re.search(pattern_donghuanyuanyin, alert_title)
        transmission_donglihuanjing = re.search(pattern_donglihuanjing, alert_title)
        transmission_OLTtuifu = re.search(pattern_OLTtuifu, alert_title)
        transmission_shujuwang = re.search(pattern_shujuwang, alert_title)
        print("开始调用", transmission_blackout)

        if transmission_blackout:
            workorder = TransmissionWorkOrder()
            # 断纤
            workorder.process_work_order(driver)
            print("调用 传输停电")

        elif power_outage_on_the_user_side:
            workorder = BankayiWorkOrder()
            # 板卡异常
            # 调用 bankayichang.py 中的 WorkOrder 方法
            workorder.process_work_order(driver)
        elif single_board_dislocation:
            workorder = GuangmokuaiWorkOrder()
            # 光模块异常
            workorder.process_work_order(driver)
            print("调用 传输单板软件")
        elif transmission_chuansongwang:
            # 传送网
            workorder = chuansongwangWorkOrder()
            workorder.process_work_order(driver)
            print("调用传送网")

        elif transmission_jike:
            # 集客
            workorder = chuansongwangWorkOrder()
            workorder.process_work_order(driver)
            print("调用集客")

        elif transmission_huayinwang:
            # 话音网
            workorder = chuansongwangWorkOrder()
            workorder.process_work_order(driver)
            print("调用话音网")

        elif transmission_donghuanyuanyin:
            # 动环原因
            workorder = chuansongwangWorkOrder()
            workorder.process_work_order(driver)
            print("调用动环原因")

        elif transmission_donglihuanjing:
            # 动力环境
            workorder = chuansongwangWorkOrder()
            workorder.process_work_order(driver)
            print("调用动力环境")

        elif transmission_shujuwang:
            # 数据网
            workorder = chuansongwangWorkOrder()
            workorder.process_work_order(driver)
            print("数据网")

        elif transmission_OLTtuifu:
            # OLT退服
            workorder =OLTWorkOrder()
            workorder.process_work_order(driver)
            print("调用传OLT退服")
        else:
            # 没有匹配到任何关键词
            # 执行默认操作或报错处理
            subprocess.run(["python", "autofile.py"])
            print("执行默认操作")