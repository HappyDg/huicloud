# -*- coding: utf-8 -*-
'''
Created on 2018年8月20日

@author: Administrator
'''
import sys
import os,time
import django
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from DappDbF2cm import views as DappDbF2cm
from django.db import transaction
class classDappDbF2cm:
    def __init__(self):
        pass
    
    
    def dft_dbi_print_excel_table_query_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_print_excel_table_query_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_user_all_projpglist_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_user_all_projpglist_req()
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_user_all_projlist_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_user_all_projlist_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_user_projpglist_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_user_projpglist_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_pgnum_inquery(self):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_pgnum_inquery()
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_user_pg_table_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_user_pg_table_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_pginfo_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_pginfo_new(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_pginfo_modify(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_pginfo_modify(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_pginfo_delete(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_pginfo_delete(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_pg_projlist_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_pg_projlist_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_project_number_inquery(self):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_project_number_inquery()
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_project_table_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_all_project_table_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_projinfo_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_projinfo_new(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_projinfo_modify(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_projinfo_modify(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_projinfo_delete(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_projinfo_delete(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_user_all_project_sitelist_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_user_all_project_sitelist_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_one_proj_sitelist_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_one_proj_sitelist_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_sitenum_inquery(self):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_sitenum_inquery()
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_sitetable_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_sitetable_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_point_get_activeinfo(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_point_get_activeinfo(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_point_set_activeinfo(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_point_set_activeInfo(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_siteInfo_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_siteInfo_new(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_siteinfo_modify(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_siteinfo_modify(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_siteinfo_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_siteinfo_delete(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_site_devlist_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_site_devlist_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_hcunum_inquery(self):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_hcunum_inquery()
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_hcutable_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_hcutable_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_devinfo_new(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_aqyc_devinfo_update(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_devinfo_update(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_aqyc_devinfo_update(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_deviceinfo_delete(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_aqyc_deviceinfo_delete(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fstt_point_product_model_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_fstt_point_config_query(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fstt_point_config_query(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_fstt_point_config_query(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fstt_point_login_history(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_fstt_point_login_history(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_projkey_delete(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result1=DappDbF2cm_view.dft_dbi_fhys_projkey_delete(inputData)
        result2=DappDbF2cm_view.dft_dbi_projinfo_delete(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return (result1 and result2)
    
    def dft_dbi_site_keyauth_delete(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result1=DappDbF2cm_view.dft_dbi_site_keyauth_delete(inputData)
        result2=DappDbF2cm_view.dft_dbi_siteinfo_delete(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return (result1 and result2)
    
    def dft_dbi_fhys_deviceinfo_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_fhys_deviceinfo_delete(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_project_userkey_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_project_userkey_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_projkey_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_projkey_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_project_keylist_proces(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_project_keylist_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_projkeyuser_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_projkeyuser_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_keynum_inquiry(self):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_keynum_inquiry()
        except Exception:
            result=0
        return result
    
    def dft_dbi_all_keytable_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_all_keytable_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_key_new_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_key_new_process(inputData)
        except Exception:
            result=False
        return result
    
    def dft_dbi_key_mod_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_key_mod_process(inputData)
        except Exception:
            result=False
        return result
    
    def dft_dbi_key_del_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_key_del_process(inputData)
        except Exception:
            result=False
        return result
    
    def dft_dbi_obj_authlist_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_obj_authlist_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_key_authlist_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_key_authlist_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_key_grant_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_key_grant_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_key_authnew_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_key_authnew_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_key_authdel_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_key_authdel_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_get_rtutable_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
        result=DappDbF2cm_view.dft_dbi_fhys_get_rtutable_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_get_otdrtable_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_fhys_get_otdrtable_req()
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    
    def dft_dbi_HCU_CPU_Query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_HCU_CPU_Query(inputData)
        except Exception:
            result ={'status':'false','auth':'true', 'msg':'数据库发生错误，请刷新页面','ret':[]}
        return result
    def dft_dbi_HCU_CPU_Binding(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_HCU_CPU_Binding(inputData)
        except Exception:
            result ={'status':'false','auth':'true', 'msg':'数据库发生错误，请刷新页面'}
        return result
    
    def dft_dbi_HCU_project_list(self):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_HCU_project_list()
        except Exception:
            result ={'status':'false','auth':'true', 'msg':'数据异常，请刷新页面','ret':[]}
        return result
    
    def dft_dbi_HCU_Get_Free_Station(self):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_HCU_Get_Free_Station()
        except Exception:
            result ={'status':'false','auth':'true', 'msg':'数据异常，请刷新页面','ret':[]}
        return result
    
    def dft_dbi_HCU_sys_config(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_HCU_sys_config(inputData)
        except Exception:
            result={'status':'true','auth':'true','ret':{},'msg':'获取参数设置失败'}
        return result
    
    def dft_dbi_HCU_sys_config_save(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_HCU_sys_config_save(inputData)
        except Exception:
            result = {'status': 'false', 'auth': 'true', 'msg': '数据异常'}
        return result
    
    def dft_dbi_HCU_Lock_Activate(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_HCU_Lock_Activate(inputData)
        except Exception:
            result = False
        return result
    
    def dft_dbi_get_device_cali(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_get_device_cali(inputData)
        except Exception:
            result = {'status':'false','auth':'true','ret':{},'msg':'数据异常'}
        return result
    
    def dft_dbi_set_device_cali(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_set_device_cali(inputData)
        except Exception:
            result = False
        return result
    
    '''WeChart App 界面入口'''
    def dft_dbi_get_device_detail(self,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.dct_classDbiL3apF2cm()
                result=DappDbF2cm_view.dft_dbi_get_device_detail(inputData)
        except Exception:
            result = {'status': 'false', 'auth': 'true', 'DevDetail': []}
        return result

class HCUF2cmDataBaseConfirm():
    
    def dft_dbi_response_HCU_data(self,socketId,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.HCUReportAndConfirm()
                result=DappDbF2cm_view.dft_dbi_response_HCU_data(socketId,inputData)
                return result
        except Exception:
            return False
    def dft_dbi_device_heart_report_data(self,socketId,inputData):
        try:
            with transaction.atomic():
                DappDbF2cm_view=DappDbF2cm.HCUReportAndConfirm()
                result=DappDbF2cm_view.dft_dbi_device_heart_report(socketId,inputData)
                return result
        except Exception:
            msg_final = {'socketid': socketId,'data': {'ToUsr': inputData['FrUsr'], 'FrUsr': inputData['ToUsr'], "CrTim": int(time.time()),'MsgTp': 'huitp_json', 'MsgId': 0X5C7F, 'MsgLn': 152, "IeCnt": {"rand":0},"FnFlg": 0}}
            return msg_final      
       
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    