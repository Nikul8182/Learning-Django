from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
        return HttpResponse('<h1>Hello This is my first Django project i am learning</h1>')


def index(request):

    students = [
          {'stdname':'Nikul Saniya', 'course':'BCA', 'age':20, 'div':'B'},
          {'stdname':'Ravi Sutariya', 'course':'BCOM', 'age':21, 'div':'C'},
          {'stdname':'Paras Zinzala', 'course':'BCA', 'age':20, 'div':'C'},
          {'stdname':'Henil Saniya', 'course':'BBA', 'age':17, 'div':'A'},
          {'stdname':'Mayur Nandaniya', 'course':'MCA', 'age':19, 'div':'A'},
          {'stdname':'Sagar Poptani', 'course':'BTECH', 'age':22, 'div':'B'},
          {'stdname':'Bhargav Saniya', 'course':'MBA', 'age':16, 'div':'B'},
    ]
    context = {
         'students' : students ,
         'page' : 'index'
    }
    return render(request, 'home/index.html', context)

def contact(request):
    context = {'page' : 'contact'}
    return render(request, 'home/contact.html', context)


def about(request):
    context = {'page' : 'about'}
    return render(request, 'home/about.html', context)