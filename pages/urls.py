from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page_viwe, name= 'home'),
    path('about/', views.about_page_view, name= 'about'),
    path('test/', views.TestPageView.as_view(), name= 'test'),
    path('change_language/<str:lang_code>/', views.change_language, name='change_language'),
]
