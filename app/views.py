from django.shortcuts import render

# Create your views here.
def industry(request):
    d={'name':'gayathri','age':21}
    return render(request,'industry.html',context=d)
