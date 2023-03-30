from django.urls import path
<<<<<<< HEAD
from .views import edit_profile, profileimage
=======
from .views import edit_profile, profileimage, post_detail
>>>>>>> Feature
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import search

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
<<<<<<< HEAD
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
=======
    path('product/<int:post_id>/', post_detail, name='product_detail'),
>>>>>>> Feature
    path('profile/', views.profile, name='profile'),
    path('perfil/editar/', edit_profile, name='editar_perfil'),
    path('perfil/editarimagen/', profileimage, name='editar_imagen'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post/', views.post, name='post'),
    path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
<<<<<<< HEAD
    path('search/', views.search, name='search'),
=======
>>>>>>> Feature
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)