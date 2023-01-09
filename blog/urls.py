from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.logIn, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('change_password/<pk>', views.change_password, name='change_password'),
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('blogs/', views.blogs, name='blogs'), 
    path('double-asteroid-redirection-test/', views.dart, name='dart'), 
    path('scifix/', views.scifix, name="scifix"),
]
