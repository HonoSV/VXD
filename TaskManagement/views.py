# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from TaskManagement import models
import json
# Create your views here.


# 锟斤拷录锟斤拷锟斤拷
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


# 锟斤拷锟斤拷锟斤拷
def welcome(request, nid):
    user = models.User.objects.filter(username=nid).first()
    prj_list = models.Project.objects.all()
    task_list = models.Task.objects.filter(P_task_id=1)
    return render(request, 'welcome.html', {'prj_list': prj_list, 'task_list': task_list, 'user': user})


# 锟斤拷目锟斤拷锟斤拷锟斤拷锟�
def project_edit(request):
    if request.method == 'GET':
        obj = models.Project.objects.all()
        return render(request, 'project_edit.html', {'obj': obj})
    elif request.method == 'POST':
        p_name = request.POST.get('P_name')
        models.Task.objects.create(P_name=p_name)
        return redirect('/taskmana/project_edit/')


# 锟芥本锟斤拷锟斤拷锟斤拷锟�
def task_edit(request):
    # if request.method == 'GET':
        obj = models.Task.objects.all()
        p_list = models.Project.objects.all()
        return render(request, 'task_edit.html', {'obj': obj, 'p_list': p_list})
    # 锟剿达拷锟斤拷删锟斤拷锟斤拷post锟斤拷钮锟斤拷锟绞诧拷应锟斤拷效
    # elif request.method == 'POST':
    #     t_name = request.POST.get('T_name')
    #     p_id = request.POST.get('P_id')
    #     models.Task.objects.create(T_name=t_name, P_task_id=p_id)
    #     return redirect('/taskmana/task_edit/')


# 锟芥本锟斤拷锟斤拷锟斤拷妫拷锟絘jax写锟斤拷锟斤拷锟斤拷
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


def detail_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        d_title = request.POST.get('d_title')
        designer = request.POST.get('designer')
        developer = request.POST.get('developer')
        manager1 = request.POST.get('manager1')
        manager2 = request.POST.get('manager2')
        flag = request.POST.get('flag')
        if d_title:
            models.Detail.objects.create(
                title=d_title,
                G_designer=designer,
                G_developer=developer,
                T_manager1=manager1,
                T_manager2=manager2,
                D_type_id=flag,
                T_process_id=1
            )
        else:
            ret['status'] = False
            ret['error'] = 'No title'
    except Exception as e:
        ret['status'] = False
        ret['error'] = 'something wrong'
        print(e)
    return HttpResponse(json.dumps(ret))


def update_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        d_id = request.POST.get('d_id')
        d_process = request.POST.get('d_process')
        d_remarks = request.POST.get('d_remarks')
        if d_id:
            models.Detail.objects.filter(id=d_id).update(T_process_id=d_process, remarks=d_remarks)
        else:
            ret['status'] = False
            ret['error'] = 'No ID'
    except Exception as e:
        ret['status'] = False
        ret['error'] = 'something wrong'
        print(e)
    return HttpResponse(json.dumps(ret))


# 锟斤拷锟斤拷锟斤拷母锟斤拷锟斤拷锟侥�
def project(request, nid):
    prj_list = models.Project.objects.all()
    task_list = models.Task.objects.filter(P_task_id=nid).all()
    return render(request, 'welcome.html', {'prj_list': prj_list, 'task_list': task_list})


# 锟斤拷锟斤拷锟斤拷陆锟斤拷锟�
def task_detail(request, nid):
    if request.method == 'GET':
        flag = nid
        obj = models.Detail.objects.filter(D_type_id=nid).all()
        process_list = models.JustPlan.objects.all()
        return render(request, 'task_detail.html', {'obj': obj, 'flag': flag, 'process_list': process_list})
    else:
        pass


def task_detail_edit(request, nid):
    if request.method == 'GET':
        flag = nid
        obj = models.Detail.objects.filter(D_type_id=nid).all()
        print(obj)
        return render(request, 'task_detail_edit.html', {'obj': obj, 'flag': flag})
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



