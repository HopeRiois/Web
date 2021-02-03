from django.urls import path
from . import views


app_name = 'datos'

urlpatterns =[
	path('', views.persona_form, name='user_insert'),
	path('<int:id>/', views.persona_form, name='user_update'),
	path('delete/<int:id>', views.persona_delete, name='user_delete'),
	path('add/', views.persona_list, name='user_list'),
]