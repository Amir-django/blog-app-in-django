from . import views
from django.urls import path

urlpatterns = [
    path('',views.postlist.as_view(),name='home'),
    path('<slug:slug>/',views.postdetails.as_view(),name='post_detail'),
]