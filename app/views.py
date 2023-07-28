from django.shortcuts import render

# Create your views here.
def data_render(request):
    d = {'name':'Satabdi','age':24}
    return render(request,'data_render.html',context=d)

def if_else(request):
    d = {'a':10, 'b' : 5}
    return render(request,'if_else.html',context=d)

def if_elif_else(request):
    d = {'a' : 10, 'b' : 5,'c': 20 }
    return render(request,'if_elif_else.html',context=d)

def nested_if(request):
    d = {'a' : 10, 'b' : 5,'c': 20 }
    return render(request,'nested_if.html',context=d)