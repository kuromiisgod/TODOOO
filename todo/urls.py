from django.contrib import admin
from django.urls import path
from todo_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list,name='todo_list'),
    path('more/<int:todo_id>', views.todo_one, name='todo_one'),
    path('more/<int:todo_id>/delete', views.todo_delete, name='todo_delete'),
    path('more/<int:todo_id>/edit', views.todo_edit, name='todo_edit'),
    path('append', views.todo_append, name='todo_append'),
    path('api',views.todo_list_api,name='todo_list_api')
]
