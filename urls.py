from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('addnew', views.addnew, name='addnew'),
	path('deleteuser/<id>', views.deleteuser, name='deleteuser'),
	path('deleted_user', views.deleted_user, name='deleted_user'),
	path('edituser/<id>', views.edituser, name='edituser'),
	path('doedit', views.doedit, name='doedit'),
	path('users', views.users, name='user'),
]
