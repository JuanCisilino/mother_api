from django.urls import path
from .views import ProductoList, UsuarioList, ProductoDetail, UsuarioDetail, home

urlpatterns = [
    path('wmapi/initProducts/',ProductoList.as_view()),
    path('wmapi/initUsers/',UsuarioList.as_view()),
    path('wmapi/users/<str:pk>',UsuarioDetail.as_view()),
    path('wmapi/prodById/<int:pk>',ProductoDetail.as_view()),
    path('', home, name='Home'),
]