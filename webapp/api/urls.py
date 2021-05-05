
from django.urls import path, include
from .views import post_list , post_create,post_detail_pk


urlpatterns = [
    path('',post_list ),
    path('create',post_create ),
    path('<int:pk>',post_detail_pk),
]