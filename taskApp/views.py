from django.shortcuts import render, HttpResponse
from taskApp import models

# Create your views here.
def home(request):
    alert={'success':0}
    # print('---------------@@@@@@@@@@@@------------------------------',request.method)
    if request.method=='POST':
        name=request.POST.get('task')
        desc=request.POST.get('desc')

        ins=models.tasks(taskname=name,taskdesc=desc)
        ins2=models.task2(taskname=name,taskdesc=desc,slug=name)
        ins.save()
        ins2.save()
        alert={'success': True}
    return render(request,'home.html',alert)



def task(request):
    no_of_posts=3
    page= request.GET.get('page')
    if page==None:
        page=1
    else:
        page=int(page)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',page)
    alltasks=models.tasks.objects.all()
    # print('--------------------------------',alltasks)
    context={'data':alltasks}
    return render(request,'tasks.html',context)


def result(request,slug):
    blog=models.tasks.objects.filter(taskname=slug).first()
    context={'blogtask':blog}
    # context={'blogtask':slug}
    return render (request,'result.html',context)
    # return HttpResponse('this is result page------- {{slug}}')
