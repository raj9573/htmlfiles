from django.shortcuts import render

# Create your views here.
def html(request):
    d={'name':'RAJ','age':23}
    return render(request,'render.html',d)