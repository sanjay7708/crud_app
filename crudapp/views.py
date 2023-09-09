from django.shortcuts import render,redirect
from . forms import student_form
from . models import student

# Create your views here.
def home(request):
    obj=student.objects.all()
    return render(request,'home.html',{'form':obj})
def add(request):
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=student_form()
    return render(request,'adddetails.html',{'form':form})

def update(request,id):
    obj=student.objects.get(id=id)
    if request.method=='POST':
        form=student_form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=student_form()
    return render(request,'update.html',{'form':form})
def delete(request,id):
    obj=student.objects.get(id=id)
    obj.delete()
    return redirect('home')
