from django.urls import path
from . import views
urlpatterns = [
    path('', views.Student_get.as_view(),name='get_student'),
    path('update-student/<int:id>', views.StudentsDetail.as_view(),name='update_student'),
    path('delete-student/<int:id>', views.DeleteStudent.as_view(),name='delete_student'),
]