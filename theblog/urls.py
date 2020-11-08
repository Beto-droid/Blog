from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    category_view

urlpatterns = [
    #  path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),  # we need to use as_view beacause its a class base views
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),   #  int:pk its a number, that automaticle django creates, its primary key of each entry
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', category_view, name='category'),


]
