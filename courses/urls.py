from django.urls import path
from courses import views

urlpatterns = [
    path('', views.course_index, name='course_index'),
    path('school=<filter_by_school>', views.course_index, name='course_index'),
    path('<int:pk>-<slug:slug>', views.course_detail, name='course_detail')
]
