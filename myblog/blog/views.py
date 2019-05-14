from django.shortcuts import render
from . import models
import os

# Create your views here.

def exesql(sql=''):
    sql = 'create table zhangzhu(id int )'
    try:
        models.angelo_db.query(sql)
    except Exception as e:
        print(e)

def index(request):
	files = os.getcwd()
	data = {
		'head':files,
		#'result':exesql(),
	}
	#exesql()
	return render(request,'index.html',data)
