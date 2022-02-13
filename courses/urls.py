from django.urls import path
from courses import views

urlpatterns = [
    path('', views.course_index, name='course_index'),
    path('<int:pk>-<slug:slug>', views.course_detail, name='course_detail')
]
