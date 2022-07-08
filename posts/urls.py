from django.urls import path

from posts import views as posts_views

urlpatterns = [
    path('<post_id>', posts_views.posts)

]
