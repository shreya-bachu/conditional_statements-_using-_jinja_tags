from django.shortcuts import render

def condition(request):

    d={'CDT':'shreya'}
    return render(request,'condition.html',context=d)

# Create your views here.
