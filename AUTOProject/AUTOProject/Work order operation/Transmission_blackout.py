"""
# Transmission_blackout.py
Author: 刘宇航
Created: 2024-01-18
Version: 1.0
License: MIT License

"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class WorkOrder:
    def process_work_order(self, driver):
        # 通过XPATH元素定位到工单操作
        operate_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/button/span[2]")))
        # 点击工单操作
        operate_button.click()
        # 通过XPATH定位到工单回复
        reply_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[1]/div/div/div[1]/div/label[3]/span[1]")))
        # 点击工单回复
        # 找到要点击的父级元素
        parent_element = driver.find_element_by_class_name('drawerTitle___3putq')
        time.sleep(2)
        reply_button.click()
        # 定位到是否现场操作选择框
        site_operation_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div/div/span[1]/input")))
        # 创建Select对象并进行选择'是'
        site_operation = Select(site_operation_select)
        site_operation.select_by_visible_text('是')
        # 定位到原因类别选择框
        reason_category_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[2]/div[1]/div/div[2]/div/div/div/div/span[1]/input")))
        # 创建Select对象并进行选择'传输'
        reason_category = Select(reason_category_select)
        reason_category.select_by_visible_text('传输')
        # 定位到故障一级原因
        fault_first_level_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/span[1]/input")
        ))
        # 创建Select对象并进行选择'电源及配套故障'
        fault_first_level_select = Select(fault_first_level_select)
        fault_first_level_select.select_by_visible_text('线路故障')
        # 定位到二级故障原因
        fault_second_level_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[3]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span[1]/input")
        ))
        # 创建Select对象并进行选择'供电局停电造成'
        fault_second_level_select = Select(fault_second_level_select)
        fault_second_level_select.select_by_visible_text('光缆故障')
        # 定位到三级故障原因
        fault_third_level_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/span[1]/input")
        ))

        # 创建Select对象并进行选择'市电停电'
        fault_third_level = Select(fault_third_level_select)
        fault_third_level.select_by_visible_text('传输线路故障导致')
        # 定位到故障处理措施结果
        handling_result_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[4]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span[1]/input")))

        # 创建Select对象并选择'市电来电后恢复'
        handling_result = Select(handling_result_select)
        handling_result.select_by_visible_text('重新调换纤芯后回复')
        # 定位到所属区域
        Belonging_Region_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[4]/div[2]/div/div[2]/div/div/div/div/span[1]/input")
        ))
        # 创建Select对象并选择'农村'
        Belonging_Region_select = Select(Belonging_Region_select)
        Belonging_Region_select.select_by_visible_text('农村')
        # 定位到故障处理结果
        fault_handling_result_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[4]/div[2]/div/div[2]/div/div/div/div/span[1]/input")
        ))
        # 创建Select对象并选择'已解决'
        fault_handling_result_select = Select(fault_handling_result_select)
        fault_handling_result_select.select_by_visible_text('已解决')
        # 定位到原因简述
        reason_summary_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[7]/div/div/div/div/div/div/div[2]/div/div/textarea")
        ))
        # 输入原因
        reason_summary_input.send_keys("经维护人员布放光缆，并重新调换纤芯后恢复正常")
        # 定位到是否存在隐患
        exist_hidden_danger_selec = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/form/div[8]/div/div/div[2]/div/div/div/div/span[1]/input")
        ))
        # 创建Select对象并选择'否'
        exist_hidden_danger_selec = Select(exist_hidden_danger_selec)
        exist_hidden_danger_selec.select_by_visible_text('否')
        # 定位到工单完成按钮
        work_order_complete_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[1]/div/div/div[3]/div/button/span")
        ))
        work_order_complete_button.click()
        time.sleep(10)
