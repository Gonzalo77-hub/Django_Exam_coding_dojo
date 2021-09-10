from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    path('administrador/', views.administrador), 
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('myaccount/<int:id>/', views.edit),
    path('edit_account/<int:num>/', views.page_edit),
    path('add_quote', views.add_quotes),
    path('quotes/', views.page_quote),
    path('add_like/<int:num>/', views.post_likes),
    path('user/<int:id>/', views.page_user),
]
