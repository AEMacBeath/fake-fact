from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('admin/', views.PostList.as_view(), name='admin'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('fake/<slug:slug>/', views.PostFakeVote.as_view(), name='post_fake'),
    path('fact/<slug:slug>/', views.PostFactVote.as_view(), name='post_fact'),
    path('message/<int:pk>/update/', views.MessageUpdateView.as_view(),
         name='message_update'),
    path('message/<int:pk>/delete/', views.MessageDeleteView.as_view(),
         name='message_delete'),
]
