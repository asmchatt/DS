# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprinttimerdeleteblob) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints

import azure.functions as func
import logging
import datetime
import json 
import requests

blueprinttimerdeleteblob = func.Blueprint()

   

@blueprinttimerdeleteblob.timer_trigger(schedule="*/1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 


def match_add_calc(x1, x2):
    return(sum(x1,x2))
def timer_trigger_deleteblob(myTimer: func.TimerRequest) -> None:
    utc_timestamp=datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed ran  at  %s  fabricated by code from DS asmita chatterjee.',utc_timestamp)
    calculated_value=match_add_calc(12,13)
    logging.info('mathemcatical calculated function return output   %s  fabricated by code from DS asmita chatterjee.',str(match_add_calc))
    # reference_chart ={
    #     'low':'B',
    #     'high':'D',
    #     'medium':'C',
    #     'unknown':'-',
    #     'critical':'F'
    # }


