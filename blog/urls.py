#
#空のビューをインポートする
from django.urls import path
from . import views


#post_list という名前の ビュー をルートURLに割り当て
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]