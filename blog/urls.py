from django.urls import path
from django.views.generic import DetailView


from . import views
from .models import Article

urlpatterns = [
#path('', DetailView.as_view(context_object_name="article", model=Article, template_name="article.html"), name='article-detail'),
path('post/new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]