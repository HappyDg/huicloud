# -*- coding: utf-8 -*-
'''
Created on 2018年8月31日

@author: Administrator
'''
class All_Golbal_Variable_Dictionary():
    def __init__(self):
        
        '''HCU Data Report Variable'''
        self.HUITPJSON_MSGID_YCDATAREPORT=0X3090
        self.HUITPJSON_MSGID_YCHEARTREPORT=0X5CFF
        self.HUITPJSON_MSGID_YCHOLOPSREPORT=0XF0C0
        self.HUITPJSON_MSGID_LOOP_TEST_REQ=0XF041
        self.HUITPJSON_MSGID_REBOOT_REQ=0XF042    
        self.HUITPJSON_MSGID_INVENTORY_REQ=0XA0A1
        
        '''HCU Data Confirm Variable'''
        self.HUITPJSON_MSGID_YCDATACONFIRM=0X3010
        self.HUITPJSON_MSGID_YCHEARTCONFIRM=0X5C7F
        self.HUITPJSON_MSGID_YCHOLOPSCONFIRM=0XF040
        self.HUITPJSON_MSGID_LOOP_TEST_RESP=0XF0C1
        self.HUITPJSON_MSGID_REBOOT_RESP=0XF0C2    
        self.HUITPJSON_MSGID_INVENTORY_CONFIRM=0XA021

GOLBALVAR=All_Golbal_Variable_Dictionary()
