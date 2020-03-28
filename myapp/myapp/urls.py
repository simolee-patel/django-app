
from django.contrib import admin
from django.urls import path
from todo.views import todoView
from todo.views import addTodo,deleteTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',todoView),
    path('addTodo/',addTodo),
    path('deleteTodo/<int:todo_id>/',deleteTodo),
]
