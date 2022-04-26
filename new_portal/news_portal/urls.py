from django.urls import path, include
from .views import PostList, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, Postsearch, subscribe

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # подключаем встроенные эндопинты для работы с локализацией
    path('', PostList.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('search/', Postsearch.as_view()),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),

]
