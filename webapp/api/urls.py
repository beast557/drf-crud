
from django.urls import path, include
from .views import (post_list , post_create,post_detail_pk, ListPosts, PostDetails)


urlpatterns = [
    # path('',post_list ),
    path('',ListPosts.as_view()),

    # path('create',post_create ),
    path('<int:id>',PostDetails.as_view()),
    # path('<int:pk>',post_detail_pk),
]