# -*- coding: utf-8 -*-
'''
Created on 2018年9月13日

@author: Administrator
'''
class Dapp_Db_Msg_Define_Dict():
    def __init__(self):
        self.HUITP_JSON_IEID_UNI_COM_CMD_TAG_SET_LAMP_WORK_MODE=13
        
        self.HCU_LOOP_TETS_REQ=1;
        self.HCU_LOOP_TETS_RESP=2
        
        self.HCU_RESTART_REQ=3
        self.HCU_RESTART_RESP=4
        
        self.HCU_NGROK_RESTART_REQ=5
        self.HCU_NGROK_RESTART_RESP=6
        
        self.HCU_SW_RESTART_REQ=7
        self.HCU_SW_RESTART_RESP=8

        self.HCU_SMART_CITY_LAMP_REQ = 9
        self.HCU_SMART_CITY_LAMP_RESP = 10
        
        
        self.HUITPJSON_MSGID_YCDATAREPORT = 0X3090
        self.HUITPJSON_MSGID_YCHEARTREPORT = 0X5CFF
        self.HUITPJSON_MSGID_YCHOLOPSREPORT = 0XF0C0
        self.HUITPJSON_MSGID_SMART_CITY_DATA_REPORT = 0X5E91
        self.HUITPJSON_MSGID_PERFORMANCE_REPORT = 0XB190

        self.HUITPJSON_MSGID_LOOP_TEST_REQ = 0XF041
        self.HUITPJSON_MSGID_REBOOT_REQ = 0XF042
        self.HUITPJSON_MSGID_INVENTORY_REQ = 0XA0A1
        self.HUITPJSON_MSGID_NGROKRES_REQ = 0XF043
        self.HUITPJSON_MSGID_SWRESTART_REQ = 0XF044
        self.HUITPJSON_MSGID_SMART_CITY_CTRL_REQ = 0X5E10

        '''HCU Data Confirm Variable'''
        self.HUITPJSON_MSGID_YCDATACONFIRM = 0X3010
        self.HUITPJSON_MSGID_YCHEARTCONFIRM = 0X5C7F
        self.HUITPJSON_MSGID_YCHOLOPSCONFIRM = 0XF040
        self.HUITPJSON_MSGID_SMART_CITY_DATA_CONFIRM = 0X5E11
        self.HUITPJSON_MSGID_PERFORMANCE_CONFIRM = 0XB110

        self.HUITPJSON_MSGID_LOOP_TEST_RESP = 0XF0C1
        self.HUITPJSON_MSGID_REBOOT_RESP = 0XF0C2
        self.HUITPJSON_MSGID_INVENTORY_CONFIRM = 0XA021
        self.HUITPJSON_MSGID_NGROKRES_RESP = 0XF0C3
        self.HUITPJSON_MSGID_SWRESTART_RESP = 0XF0C4
        self.HUITPJSON_MSGID_SMART_CITY_CTRL_RESP = 0X5E90

GOLBALVAR=Dapp_Db_Msg_Define_Dict()