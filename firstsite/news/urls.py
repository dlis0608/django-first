from django.urls import path

from .views import *

urlpatterns = [
    # path('', index, name='home'),

    path('', HomeNews.as_view(), name='home'),
    path('cat/<int:category_id>/', CategoryNews.as_view(), name='category'),
    path('news/<int:pk>/', SingleNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('news/register/', register, name='register'),
    path('news/login/', user_login, name='login'),
    path('news/logout/', user_logout, name='logout'),
    path('contact/', contact_form, name='contact'),

]
