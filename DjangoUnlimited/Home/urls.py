from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_job', views.create_job, name='create_job'),
    path('view_jobs', views.view_jobs, name='view_jobs'),
    path('my_applications', views.my_applications, name='my_applications'),
    path('job_details/<int:id>', views.job_details, name='job_details'),
    path('edit_job/<int:id>', views.edit_job, name='edit_job'),
    path('delete_job/<int:id>', views.delete_job, name='delete_job'),
    path('close_job/<int:id>', views.close_job, name='close_job'),
    path('view_students', views.view_students, name='view_students'),
    path('student_details/<int:id>', views.student_details, name='student_details'),
    path('filter_students', views.filter_students, name='filter_students'),
    path('news', views.news, name='news')
]
