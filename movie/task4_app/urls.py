from django.urls import path
from . import views
app_name = 'task4_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:task4_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
 ]