# -*- encoding=utf8 -*-
__author__ = "Hiram"

from airtest.core.api import *
import time

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# poco(text="学习强国").click()

def login(account,password):
    poco(name="cn.xuexi.android:id/et_phone_input").set_text(account)
    poco(name="cn.xuexi.android:id/et_pwd_login").set_text(password)
    poco(name="cn.xuexi.android:id/btn_next").click()
    sleep(5.0)

    poco(name="cn.xuexi.android:id/comm_head_xuexi_mine").click()
    poco(name="cn.xuexi.android:id/my_setting").click()
    poco(text="退出登录").click()
    poco(name="android:id/button1").click()
    sleep(3.0)

with open ('accounts.txt',mode='r') as f:
    try:
        while True:
            accountTxt = f.readline()
            account,password=accountTxt.split('#')
            login(account,password[:-1])
    except:
        print('完成全部账号登录')
