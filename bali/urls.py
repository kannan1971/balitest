from django.urls import path
from .views import bali_view

app_name='bali'

urlpatterns = [
    path('', bali_view, name = 'bali-view'),
    # path('slide',slide_view, name ='slide-view')

]
