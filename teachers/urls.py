from django.urls import path
from . import views
urlpatterns = [
    path('',views.teachers_list,name='all-teachers'),
    path('add-teacher/',views.add_teacher,name='all-new-teacher'),
    path('update-teacher/<int:id>',views.update_feature,name='update-teacher'),
    path('delete_teacher/<int:id>',views.delete_teacher,name='delete_teacher'),
]