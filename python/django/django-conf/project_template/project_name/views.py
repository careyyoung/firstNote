# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, '{{project_name}}/hello_project.html')
