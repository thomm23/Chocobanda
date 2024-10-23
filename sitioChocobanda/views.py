from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class PaginaPrincipal(View): 
    def get(self,request):
        context={

        }
        return render(request,'home.html',context)