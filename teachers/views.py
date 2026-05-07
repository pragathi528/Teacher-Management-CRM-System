from django.shortcuts import render, redirect
from .models import Teachers
# Create your views here.

def teachers_list(request):
    teachers = Teachers.objects.all()
    return render(request, 'index.html',{'allteachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teachers(
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect('all-teachers')
    return render(request,'index.html')

def update_feature(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teachers(
            id = id,
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect('all-teachers')
    return render(request,'index.html',{'teacher':teacher})

def delete_teacher(request,id):
    teacher = Teachers.objects.filter(id=id)
    teacher.delete()
    return redirect('all-teachers')