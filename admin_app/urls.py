from django.urls import path
from.import views

urlpatterns = [
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_create',views.admin_create,name='admin_create'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_edit/<id>',views.admin_edit,name='admin_edit'),
    path('admin_delete/<id>',views.admin_delete,name='admin_delete'),
    path('admin_logout',views.admin_logout_button,name='admin_logout'),
    path('admin_search',views.admin_search,name='admin_search'),
]
