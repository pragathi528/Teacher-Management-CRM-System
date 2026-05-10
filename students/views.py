from django.shortcuts import render, redirect
from django.http import Http404
from .serializer import StudentSerializer
from .models import Students
from rest_framework.views import APIView

# Create your views here.
class Student_get(APIView):
    def get(self,request):
        students = Students.objects.all()
        return render(request, "students.html",{"students": students})
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('get_student')

class StudentsDetail(APIView):
    def post(self, request, id):
        student = Students.objects.get(id=id)
        serializer  = StudentSerializer(student,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return redirect('get_student')
    
class DeleteStudent(APIView):
    def post(self, request, id):
        student = Students.objects.get(id=id)
        student.delete()
        return redirect('get_student') 

