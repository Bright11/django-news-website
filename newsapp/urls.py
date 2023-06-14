from django.urls import path

from . import views

app_name="newsapp"
urlpatterns = [
    path('', views.index.as_view(),name='index'),
    path("category/<int:pk>/",views.category.as_view(),name="category")
]
