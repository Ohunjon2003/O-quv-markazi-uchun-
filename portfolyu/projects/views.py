from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def projects(request):

    projects = Project.objects.all()
    context = {

        'projects':projects
    }
    return render(request,'projects/projects.html',context)


def project(request,id):
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        messages.warning(request,"Bu loyiha mavjud emas")
        return redirect('projects')
    context = {
        'project':project

    }
    return render(request,'projects/project.html',context)


@login_required(login_url='login')
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user.profil
            project.save()
            return redirect('projects')
    form = ProjectForm()
    context = {
        'form':form
    }
    return render(request,'projects/project_add.html',context)


@login_required(login_url='login')
def project_edit(request, id):
    try:
        project = Project.objects.get(id=id,user=request.user.profil)
    except Project.DoesNotExist:
        messages.error(request,"Siz faqat o'zingizga tegishli loyihani o'chirolasiz")
        return redirect('projects')
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form':form
    }
    return render(request,'projects/project_add.html',context)
@login_required(login_url='login')
def project_delete(request,id):
    profil = request.user.profil
    try:
        profil.project_set.get(id=id)
    except Project.DoesNotExist:
        messages.warning(request,"Siz faqat o'zingizga tegishli loyihalarnigina o'chiraolasiz")
        return redirect('account')
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects')