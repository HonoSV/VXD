from django.shortcuts import render, redirect
from TaskManagement import  models
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_info = request.POST.get('username')
        pwd_info = request.POST.get('password')
        flag = models.User.objects.filter(username=user_info, password=pwd_info).first()
        if flag:
            final = '/taskmana/welcome-' + flag.username + '/'
            return redirect(final)
        else:
            return render(request, 'login.html')
    else:
        redirect('/taskmana/login/')


def welcome(request, nid):
        user = models.User.objects.filter(username=nid).first()
        prj_list = models.Project.objects.all()
        task_list = models.Task.objects.filter(P_task_id=1)
        return render(request, 'welcome.html', {'prj_list': prj_list, 'task_list': task_list, 'user': user})
