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


def project_edit(request):
    if request.method == 'GET':
        obj = models.Project.objects.all()
        return render(request, 'project_edit.html', {'obj': obj})
    elif request.method == 'POST':
        p_name = request.POST.get('P_name')
        models.Task.objects.create(P_name=p_name)
        return redirect('/taskmana/project_edit/')


def task_edit(request):
    if request.method == 'GET':
        obj = models.Task.objects.all()
        p_list = models.Project.objects.all()
        return render(request, 'task_edit.html', {'obj': obj, 'p_list': p_list})
    elif request.method == 'POST':
        t_name = request.POST.get('T_name')
        p_id = request.POST.get('P_id')
        models.Task.objects.create(T_name=t_name, P_task_id=p_id)
        return redirect('/taskmana/task_edit/')