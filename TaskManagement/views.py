from django.shortcuts import render, redirect, HttpResponse
from TaskManagement import models
import json
# Create your views here.


# 登录界面
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'error_msg': ''})
    elif request.method == 'POST':
        user_info = request.POST.get('username')
        pwd_info = request.POST.get('password')
        flag = models.User.objects.filter(username=user_info, password=pwd_info).first()
        if flag:
            final = '/taskmana/welcome-' + flag.username + '/'
            return redirect(final)
        else:
            return render(request, 'login.html', {'error_msg': 'RTX or password is error'})
    else:
        redirect('/taskmana/login/')


# 主界面
def welcome(request, nid):
    user = models.User.objects.filter(username=nid).first()
    prj_list = models.Project.objects.all()
    task_list = models.Task.objects.filter(P_task_id=1)
    return render(request, 'welcome.html', {'prj_list': prj_list, 'task_list': task_list, 'user': user})


# 项目管理界面
def project_edit(request):
    if request.method == 'GET':
        obj = models.Project.objects.all()
        return render(request, 'project_edit.html', {'obj': obj})
    elif request.method == 'POST':
        p_name = request.POST.get('P_name')
        models.Task.objects.create(P_name=p_name)
        return redirect('/taskmana/project_edit/')


# 版本管理界面
def task_edit(request):
    # if request.method == 'GET':
        obj = models.Task.objects.all()
        p_list = models.Project.objects.all()
        return render(request, 'task_edit.html', {'obj': obj, 'p_list': p_list})
    # 此处因删除掉post按钮，故不应生效
    # elif request.method == 'POST':
    #     t_name = request.POST.get('T_name')
    #     p_id = request.POST.get('P_id')
    #     models.Task.objects.create(T_name=t_name, P_task_id=p_id)
    #     return redirect('/taskmana/task_edit/')


# 版本管理界面，通过ajax写入数据
def test_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        t_name = request.POST.get('t_name')
        sel = request.POST.get('sel')
        if t_name:
            models.Task.objects.create(T_name=t_name, P_task_id=sel)
        else:
            ret['status'] = False
            ret['error'] = 'No task name'
    except Exception as e:
        ret['status'] = False
        ret['error'] = e
    return HttpResponse(json.dumps(ret))


def project_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        p_name = request.POST.get('p_name')
        if p_name:
            models.Project.objects.create(P_name=p_name)
        else:
            ret['status'] = False
            ret['error'] = 'No task name'
    except Exception as e:
        ret['status'] = False
        ret['error'] = e
    return HttpResponse(json.dumps(ret))


# 主界面的各子项目
def project(request, nid):
    prj_list = models.Project.objects.all()
    task_list = models.Task.objects.filter(P_task_id=nid).all()
    return render(request, 'welcome.html', {'prj_list': prj_list, 'task_list': task_list})


# 任务更新界面
def task_detail(request, nid):
    if request.method == 'GET':
        obj = models.Detail.objects.filter(id=nid).all()
        return render(request, 'task_detail.html', {'obj': obj})
    else:
        pass


def task_delete(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        status = "Delete Success"
        result = "Error"
        flag = models.Task.objects.filter(id=task_id).delete()
        if flag:
            return HttpResponse(
                json.dumps({
                    "status": status
                })
            )
        else:
            return HttpResponse(
                json.dumps({
                    "status": result
                })

            )


def project_delete(request):
    if request.method == "POST":
        project_id = request.POST.get('project_id')
        status = "Delete Success"
        result = "Error"
        flag = models.Project.objects.filter(id=project_id).delete()
        if flag:
            return HttpResponse(
                json.dumps({
                    "status": status
                })
            )
        else:
            return HttpResponse(
                json.dumps({
                    "status": result
                })

            )