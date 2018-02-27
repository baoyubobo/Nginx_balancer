from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q
from lazy_balancer.views import is_auth
from proxy.models import proxy_config,upstream_config
from settings.models import system_settings
from nginx.views import *
from nginx.ip import *
import json
import uuid
import time
import os



#from pyhive import hive
#from TCLIService.ttypes import TOperationState



@login_required(login_url="/login/")
def view(request):   
    return render_to_response('hive/view.html')
    pass


@is_auth
def hive_result_1(request):
    try:
        cursor = hive.connect(host='localhost',port=10000, database='default').cursor()
        cursor.execute('use hive_1208')
        cursor.execute('select host,count(host) as c from td_log_analyze group by host order by  c desc ')
        #print(cursor.fetchone())
        #print(cursor.fetchall())
        res=cursor.fetchall()
        outer_res=''
        for r in res:
            outer_res += str(r)
            outer_res += '\n'
        

        result_body = {"inner":"","outer":""}



        result_body['outer'] = outer_res
        result_body['inner'] = "Hive HQL inner result 1"                
                
       

        context = { "flag":"Success" , "result_body":result_body  }
    except Exception, e:
        context = { "flag":"Error","context":str(e) }

    return HttpResponse(json.dumps(context))
    pass


@is_auth
def hive_result_2(request):
    try:

        cursor = hive.connect(host='localhost',port=10000, database='default').cursor()
        cursor.execute('select * from t_hive')
        #print(cursor.fetchone())
        #print(cursor.fetchall())
        res=cursor.fetchall()

        result_body = {"inner":"","outer":""}

        result_body['outer'] = "Hive HQL outer result 2"
        result_body['inner'] = res         
                
       

        context = { "flag":"Success" , "result_body":result_body  }
    except Exception, e:
        context = { "flag":"Error","context":str(e) }

    return HttpResponse(json.dumps(context))
    pass

@is_auth
def hive_result_3(request):
    try:
        result_body = {"inner":"","outer":""}

        result_body['outer'] = "Hive HQL outer result 333333333333333333"
        result_body['inner'] = "Hive HQL inner result 333333333333333333"         
                
       

        context = { "flag":"Success" , "result_body":result_body  }
    except Exception, e:
        context = { "flag":"Error","context":str(e) }

    return HttpResponse(json.dumps(context))
    pass
