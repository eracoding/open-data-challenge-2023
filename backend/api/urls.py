from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('gptneo/', views.GptNeoListView.as_view()),
    path('category/', views.CategoryListView.as_view()),
    path("category/create", views.CategoryCreateView.as_view()),
    path("category/create/<int:pk>/", views.CategoryCreateView.as_view()),

    path("category/delete", views.DeleteCategory.as_view()),
    path("status/", views.StatusListView.as_view()),
    path("wikikeys/", views.WikiKeysListView.as_view()),
]
