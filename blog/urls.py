from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('fake/<slug:slug>', views.PostFakeVote.as_view(), name='post_fake'),
    path('fact/<slug:slug>', views.PostFactVote.as_view(), name='post_fact'),
]
