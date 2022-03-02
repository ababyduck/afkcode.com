from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    # path('articles/<int:year>/', views.blog_detail, name='blog_years'),
    # path('articles/<int:year>/<int:month>', views.blog_detail, name='blog_months'),
    path('blog/<int:year>/<int:month>/<int:pk>-<slug:slug>', views.blog_detail, name='blog_detail'),
    path('category/<category>/', views.blog_category, name='blog_category'),
]
