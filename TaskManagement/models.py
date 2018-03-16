from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    P_name = models.CharField(max_length=64)


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    P_task = models.ForeignKey('Project', on_delete=models.CASCADE)
    T_name = models.CharField(max_length=64, unique=True)


class JustPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    plan = models.CharField(max_length=64)


class Detail(models.Model):
    id = models.IntegerField(primary_key=True)
    D_type = models.ForeignKey('Task', to_field='T_name', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    G_designer = models.CharField(max_length=64, null=True)
    G_developer = models.CharField(max_length=64, null=True)
    T_manager1 = models.CharField(max_length=64, null=True)
    T_manager2 = models.CharField(max_length=64, null=True)
    T_process = models.ForeignKey('JustPlan', null=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=64, null=True)
    U_time = models.DateTimeField(auto_now=True, null=True)






