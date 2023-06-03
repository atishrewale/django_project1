from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee,Office, EmployeeFomr,OfficeFomr
from django.core import serializers
from django.forms.models import model_to_dict
from django.core import serializers
# Create your views here.


def home(request):
    officeform = OfficeFomr()
    employeeform = EmployeeFomr()
    context = {
        "officeform" : officeform,
        "employeeform" : employeeform
    }

    return render(request,'index.html',context)



def officecrud(request):
    if request.method == "POST":
        print(request.POST)
        officeForm = OfficeFomr(request.POST)
        office = officeForm.save()

        return JsonResponse(model_to_dict(office) ,safe=False)
    



def employeecrud(request):
    if request.method == "POST":
        print(request.POST)
        employeeForm = EmployeeFomr(request.POST)
        employee = employeeForm.save()
        office = employee.office
        print(office)
        officeJson = model_to_dict(office)

        response = model_to_dict(employee)
        response['office'] = officeJson

        return JsonResponse(response)
    

def getalloffices(request):
    offices = Office.objects.all()
    data = serializers.serialize("json",offices)
    return JsonResponse(data,safe=False)
    

def getallemloyees(request):
    emloyees = Employee.objects.all()
    data = serializers.serialize("json" , emloyees , use_natural_foreign_keys=True )
    return JsonResponse(data,safe=False)
    

def showEmployeePage(request):
    employeeform = EmployeeFomr()
    context = {
        "employeeform" : employeeform
    }
    return render(request,'employee-page.html',context)

def showOfficePage(request):
    officeform = OfficeFomr()
    context = {
        "officeform" : officeform,
    }
    return render(request,'office-page.html',context)

