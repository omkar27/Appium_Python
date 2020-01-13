

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from coverage.annotate import os
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "deviceName": "Nexus 5X",
    "platformName": "Android",
    "version" : "8.0.0",
    "app": "E://vaultize-android-app-debug.apk",
   # "appPackage":"com.asus.filemanager",
    #"appActivity":"com.asus.filemanager.activity.FileManagerGetContent",
    "realDevice": True
   # "autoGrantPermissions":True
}
#os.system("adb shell am start -n com.asus.filemanager/com.asus.filemanager.activity.FileManagerActivity")

# def start_app():
#     os.system("adb shell am start -n com.vaultize.mobility/com.vaultize.mobility.view.SplashScreen")

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


driver.implicitly_wait(15)
pop = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]')
pop.click()
driver.implicitly_wait(15)
driver.find_element_by_id('com.vaultize.mobility:id/textUsername').send_keys('dummyomkar@gmail.com')
driver.implicitly_wait(15)
driver.find_element_by_id('com.vaultize.mobility:id/textPasswd').send_keys('vault@123')
driver.implicitly_wait(15)
driver.find_element_by_id('com.vaultize.mobility:id/textUrl').send_keys('https://pune.vaultize.com')
driver.implicitly_wait(15)
driver.find_element_by_id('com.vaultize.mobility:id/buttonLogin').click()
driver.implicitly_wait(15)
#pop = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout')
#driver.set_value(pop,'ALLOW')
driver.implicitly_wait(15)
actions = TouchAction(driver)
driver.implicitly_wait(15)
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
actions.tap(driver.find_element_by_id('com.vaultize.mobility:id/buttonOne'))
driver.implicitly_wait(15)
actions.perform()
driver.implicitly_wait(20)
actions.scroll_from_element(element, 10, 100)
actions.scroll(10, 100)
actions.perform()

#
# # one = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridLayout[2]/android.widget.Button[1]')
#driver.find_element_by_id('com.vaultize.mobility:id/indicatorOne').send_keys("1")
# driver.implicitly_wait(15)
# driver.find_element_by_id('com.vaultize.mobility:id/indicatorTwo').send_keys("1")
# driver.implicitly_wait(15)
# driver.find_element_by_id('com.vaultize.mobility:id/indicatorThree').send_keys("1")
# driver.implicitly_wait(15)
# driver.find_element_by_id('com.vaultize.mobility:id/indicatorFour').send_keys("1")
# driver.find_element_by_id('com.vaultize.mobility:id/buttonOne').click()
# driver.find_element_by_id('com.vaultize.mobility:id/buttonOne').click()
# driver.find_element_by_id('com.vaultize.mobility:id/buttonOne').click()
# one.click()
# one.click()
# one.click()
# one.click()




