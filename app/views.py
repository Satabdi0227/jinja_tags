from django.shortcuts import render

# Create your views here.
def data_render(request):
    d = {'name':'Satabdi','age':24}
    return render(request,'data_render.html',context=d)

def if_else(request):
    d = {'a':10, 'b' : 5}
    return render(request,'if_else.html',context=d)