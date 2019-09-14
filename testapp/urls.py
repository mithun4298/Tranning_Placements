from django.urls import path
from testapp import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login, name = "login"),
    path('info/', views.infoo, name = "info"),
    path('logout/', views.logout, name = "logout"),
    path('studentform/', views.student_form, name = "student_form"),
    path('about/', views.about, name = "about"),
    path('selectstudent/', views.select_student, name = "selectstudent"),
    path('sdetails', views.sdetails, name = 'sdetails')


]
