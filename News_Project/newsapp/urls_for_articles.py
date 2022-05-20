from django.urls import path
from .views import PostsList, PostDetail, PostCreate_for_articles, PostUpdate, PostDelete

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate_for_articles.as_view(), name='post_create_for_articles'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]