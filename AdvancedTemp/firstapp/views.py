from django.shortcuts import render,redirect
from firstapp.models import *
from firstapp.forms import *
# Create your views here.

def index(request):
    employee_data=Employee.objects.all()
    context={'emp_data':employee_data}
    return render(request,'firstapp/index.html',context=context)

def formIndex(request):
    if request.method=="POST":
        form=empForm(request.POST)
        if form.is_valid():
            print("the form is valid")
            form.save(commit=True)
            return redirect('form')
    else:
        form=empForm()
    context={"form":form}
    return render(request,'firstapp/form.html',context=context)


def business(request):
    count=int(request.COOKIES.get('count',0))
    new=count+1
    context={'new':new}
    response=render(request,'firstapp/business.html',context=context)
    response.set_cookie('count',new,max_age=60)
    return response

def info(request):
    return render(request,'firstapp/info.html')

def portfolio(request):
    return render(request,'firstapp/portfolio.html')