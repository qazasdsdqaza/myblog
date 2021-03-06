from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(prefix='blog', viewset=views.BLogViewset)


urlpatterns = [
    path('', views.Index.as_view()),
    path('index.html/', views.Index.as_view(), name='home'),
    path('about.html/', views.AboutView.as_view(), name='about'),
    path('detail.html/<int:article_id>/', views.DetailPage.as_view(), name='detail'),
    # path('login.html/', views.LoginView.as_view(), name='login'),
    # path('register.html/', views.RegisterAPIView.as_view(), name='register'),
    # path('logout.html/', views.LogoutAPIView.as_view(), name='logout'),
    path('archive/<int:year>/<int:month>/', views.Archive.as_view(), name='archive'),
    path('category/<int:category_id>/', views.Category.as_view(), name='category'),
    path('comments/', views.Comments.as_view(), name='comments'),
    path('', include(routers.urls)),



]
