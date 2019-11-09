#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Jie Xiang'

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

# 1-满减券 2-折扣券 3-立减券 4-包邮券
voucherType = 1
# 创建多少张优惠券
voucherSetCount = 2

rebateVoucher = {
    # 优惠券面额
    "voucherValue": 5,
    # 优惠券门槛
    "voucherThreshold": 5,
    # 优惠券中文名
    "voucherName_CN": "满RM5减RM5",
    # 优惠券英文名
    "voucherName_EN": "Buy RM5 get RM5 off",
    # 优惠券张数
    "voucherCount": 5,
    # 每人限领几张
    "voucherForOnePerson": 1,
    # 每天限领几张
    "voucherForOneDay": 5,
    # 生效时间
    "voucherEffectiveTime": "2019-11-11 00:00:00",
    # 失效时间
    "voucherInvalidTime": "2019-11-11 23:59:59",
    # 优惠券中文描述
    "voucherDesName_CN": "社群晒单狂撒券",
    # 优惠券英文描述
    "voucherDesName_EN": "Giveaway for group chats"}

discountVoucher = {
    # 优惠券折扣
    "voucherDiscount": 8,
    "voucherName_CN": "8折券",
    "voucherName_EN": "20% Off",
    "voucherCount": 50,
    "voucherForOnePerson": 1,
    "voucherForOneDay": 50,
    "voucherEffectiveTime": "2019-11-11 00:00:00",
    "voucherInvalidTime": "2019-11-11 23:59:59",
    "voucherDesName_CN": "社群晒单狂撒券",
    "voucherDesName_EN": "Giveaway for group chats"}


def setRebateVoucher():
    # 新增优惠券
    chromeBrowser.find_element_by_xpath('//*[@class="layout-content-box"]/div/div/div/div[2]/div/div/button').click()
    time.sleep(1)

    # 输入优惠券中文名
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[2]/div/div/input').send_keys(rebateVoucher["voucherName_CN"])
    time.sleep(1)

    # 输入优惠券英文名
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[3]/div/div/input').send_keys(rebateVoucher["voucherName_EN"])
    time.sleep(1)

    # 输入优惠券总发行量
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[4]/div/div/div/input').clear()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[4]/div/div/div/input').send_keys(rebateVoucher["voucherCount"])
    time.sleep(1)

    # 输入优惠券每人限领
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[5]/div/div/div/input').clear()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[5]/div/div/div/input').send_keys(rebateVoucher["voucherForOnePerson"])
    time.sleep(1)

    # 输入优惠券每日限领
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[6]/div/div/div/input').clear()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[6]/div/div/div/input').send_keys(rebateVoucher["voucherForOneDay"])
    time.sleep(1)

    # 输入优惠券面值
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[8]/div/div/input').send_keys(rebateVoucher["voucherValue"])
    time.sleep(1)

    # 输入优惠券使用门槛
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[9]/div/div/div/input').clear()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[9]/div/div/div/input').send_keys(rebateVoucher["voucherThreshold"])
    time.sleep(1)

    # 输入优惠券日期范围-生效时间
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[10]/div/div/label/span[2]/div/input').send_keys(rebateVoucher["voucherEffectiveTime"])
    time.sleep(1)

    # 输入优惠券日期范围-失效时间
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[10]/div/div/label/span[2]/div/input[2]').send_keys(rebateVoucher["voucherInvalidTime"])
    time.sleep(1)

    # 输入优惠券会员级别
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label/span/span').click()
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label[2]/span/span').click()
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label[3]/span/span').click()
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label[4]/span/span').click()

    # 输入优惠券中文描述
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[13]/div/div/textarea').send_keys(rebateVoucher["voucherDesName_CN"])
    time.sleep(1)

    # 输入优惠券英文描述
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[14]/div/div/textarea').send_keys(rebateVoucher["voucherDesName_EN"])
    time.sleep(1)

    # 点击确认保存
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[15]/div/button').click()
    time.sleep(2)


def setDiscountVoucher():
    # 新增优惠券
    chromeBrowser.find_element_by_xpath('//*[@class="layout-content-box"]/div/div/div/div[2]/div/div/button').click()
    time.sleep(1)

    # 点击选择满减券
    chromeBrowser.find_element_by_xpath('//*[@class="app-container"]/form/div/div/div').click()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-select-dropdown el-popper"]/div/div/ul/li[2]/span').click()
    time.sleep(1)

    # 输入优惠券中文名
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[2]/div/div/input').send_keys(discountVoucher["voucherName_CN"])
    time.sleep(1)

    # 输入优惠券英文名
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[3]/div/div/input').send_keys(discountVoucher["voucherName_EN"])
    time.sleep(1)

    # 输入优惠券总发行量
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[4]/div/div/div/input').clear()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[4]/div/div/div/input').send_keys(discountVoucher["voucherCount"])
    time.sleep(1)

    # 输入优惠券每人限领
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[5]/div/div/div/input').clear()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[5]/div/div/div/input').send_keys(discountVoucher["voucherForOnePerson"])
    time.sleep(1)

    # 输入优惠券每日限领
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[6]/div/div/div/input').clear()
    time.sleep(1)
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[6]/div/div/div/input').send_keys(discountVoucher["voucherForOneDay"])
    time.sleep(1)

    # 输入优惠券折扣
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[8]/div/div/input').send_keys(discountVoucher["voucherDiscount"])
    time.sleep(1)

    # 输入优惠券日期范围-生效时间
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[10]/div/div/label/span[2]/div/input').send_keys(discountVoucher["voucherEffectiveTime"])
    time.sleep(1)

    # 输入优惠券日期范围-失效时间
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[10]/div/div/label/span[2]/div/input[2]').send_keys(discountVoucher["voucherInvalidTime"])
    time.sleep(1)

    # 输入优惠券会员级别
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label/span/span').click()
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label[2]/span/span').click()
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label[3]/span/span').click()
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[12]/div/div/label[4]/span/span').click()

    # 输入优惠券中文描述
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[13]/div/div/textarea').send_keys(discountVoucher["voucherDesName_CN"])
    time.sleep(1)

    # 输入优惠券英文描述
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[14]/div/div/textarea').send_keys(discountVoucher["voucherDesName_EN"])
    time.sleep(1)

    # 点击确认保存
    chromeBrowser.find_element_by_xpath('//*[@class="el-form el-form--label-right"]/div[15]/div/button').click()
    time.sleep(2)


if __name__ == "__main__":

    chromeBrowser = webdriver.Chrome()
    # chromeBrowser.get('https://admin.fingo.shop/#/operation/timeLimitList')
    chromeBrowser.get('https://admin.fingo.shop')
    time.sleep(2)

    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div/div/div/input').send_keys(
            'Dean')
    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div[2]/div/div/input').send_keys(
            'fingo666')
    # 点击登陆
    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div[3]/div/button').click()

    time.sleep(3)

    # 点击折叠打开运营管理
    chromeBrowser.find_element_by_xpath(
        '//*[@class="layout-nav-wrapper"]/div/ul/li[8]/div').click()

    time.sleep(1)
    # 跳转限时特价
    chromeBrowser.find_element_by_xpath(
        '//*[@class="layout-nav-wrapper"]/div/ul/li[8]/ul/li[7]/a/span').click()
    time.sleep(1)

    if voucherType == 1:
        if (voucherSetCount == 1):
            setRebateVoucher()
        else:
            for i in range(0, voucherSetCount):
                setRebateVoucher()
    elif voucherType == 2:
        if (voucherSetCount == 1):
            setDiscountVoucher()
        else:
            for i in range(0, voucherSetCount):
                setDiscountVoucher()
    elif voucherType == 3:
        pass
    else:
        pass
