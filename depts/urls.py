from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.home, name = "home"),
    path('comp/', views.comp, name = "comp"),
    path('IT/', views.IT, name = "IT"),
    path('EXTC/', views.EXTC, name = "EXTC"),
    path('FE/', views.FE, name = "FE"),
    path('mech/', views.mech, name = "mech"),
    path('instru/', views.instru, name = "instru"),
    path('about/', views.about, name = "about"),
    path('dept/', views.dept, name = "dept"),
    path('comp/staff/', views.compstaff, name = "compstaff")
]
