from django.shortcuts import render,redirect
from monitor.models import *
from django.http import *
import smtplib
from urllib.parse import quote_plus
from django.contrib import messages
from faker import Faker


# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from monitor.models import IOT


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()
import re
import random
from faker import Faker

from monitor.models import IOT


fakegen = Faker()

def populate(self):
    for i in range(10):
        levels = ['5', '10', '15','20','25','30','35','40','45','50','100']
        device_current=levels[random.randint(0, 10)]
        levels1 = ['5', '10', '15','20','25','30','35','40','45','50','100']
        device_voltage= levels1[random.randint(3, 10)]
        levels2 = ['1', '10', '20','30','40','50','60','70','80','90','100']
        device_kw= levels2[random.randint(0, 10)]
        levels3 = ['1', '2', '3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
        hours= levels3[random.randint(0, 22)]
        todo_item = IOT.objects.update(device_current=device_current, device_voltage=device_voltage,device_kw=device_kw,hours=hours)
        print(todo_item)
        return redirect('/home')
if __name__ == '__main__':
    print('Populating data...')
    populate(20)
    print('Populating complete')



class CartItemViews(APIView):
    def get(self, request, id=None):
        if id:
            item = IOT.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = IOT.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

def smtp_sendmail(email,sub,body):
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.login("itsamareshv@gmail.com","Your KEY")
	message=f"subject:{sub}\n\n{body}"
	server.sendmail("itsamareshv@gmail.com",email,message)
	server.quit()
	print("Mail Sent")

def submit(req):

    vol= IOT.objects.all()
    for i in vol:
        v=i.device_voltage
        print(v)
    # str(MyModel.objects.all().query)

    if float(v) >9:
        temp=list(IOT.objects.filter(device_voltage=v).values())
        print(temp)
        email="ajay9818ajju@gmail.com"
        subject="Device Getting Heated"
        body="Plese find the parameters attached below",temp
        smtp_sendmail(email,subject,body)
        return redirect('/home')

def login(request):
	return render(request,'login.html')


def loginpage(request):
	un=(request.POST.get('username'))
	if(un):
		if(checkemail(un)):
			if(request.POST.get('password') == request.POST.get('password')):
				a = Login(username = request.POST.get('username'),password = request.POST.get('password'))
				a.save()
				return render(request,"index.html")
			else:
				return render(request,'register.html',{'error':"password doesnt match"})
		else:
			return render(request,'register.html',{'error1':"Enter a valid email"})
	else:
		return render(request,'login.html')



def checkemail(username):
	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	if(re.search(regex,username)):
		return True
	else:
		return False

def loggedin(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	print("--------------->",username,password)
	x=Login.objects.all().values()
	username_list=[]
	for i in x:
		username_list.append(i['username'])
	print(username_list)
	if(username in username_list):
		a = Login.objects.get(username = username)
		if a.password == password:
			request.session['id']=username
			return render(request,'index.html')
		else:
			return render(request,'login.html',{'error':'Incorrect credentials'})
	else:
		return render(request,'register.html')
	return HttpResponse()

def index(request):
    all_iot = IOT.objects.all
    context = {'all_iot': all_iot}
    return render(request, "index.html",context)

def delete_iot(request, device_id):
    iot_delete =IOT.objects.get(device_id=device_id)
    iot_delete.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect('/home')
def addiot(req):

    return render(req, "addiot.html")

def newiot(req):
    device_name = req.POST["device_name"]
    device_current= req.POST["device_current"]
    device_voltage= req.POST["device_voltage"]
    device_kw= req.POST["device_kw"]
    hours= req.POST["hours"]
    iotinfo =IOT(device_name=device_name,device_current=device_current,device_voltage=device_voltage,device_kw=device_kw,hours=hours)
    iotinfo.save()
    return render(req, "addiot.html")
