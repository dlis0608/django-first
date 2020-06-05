from django.urls import path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('cat/<int:category_id>/', CategoryNews.as_view(), name='category'),
    path('news/<int:pk>/', SingleNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
