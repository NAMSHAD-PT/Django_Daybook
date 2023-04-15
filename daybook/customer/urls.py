from django.urls import path
from .import views

urlpatterns=[
    path('register',views.Register,name='register'),
    path('',views.home,name='home'),
    path('addcontact',views.addContact,name='addcontact'),
    path('editcontact/<int:id>',views.editContact,name='editcontact'),
    path('deletecontact/<int:id>',views.deleteContact,name='deletecontact'),
    path('login',views.login_customer,name='login'),
    path('logout',views.logout_customer,name='logout'),
    path('expence/<int:id>',views.expence,name='expence'),
    path('addexpence',views.addExpence,name='addexpence'),
    path('editexpence/<int:id>',views.editExpence,name='editexpence'),
    path('delete/<int:id>',views.delete,name='delete'),
]