from django.urls import path
from .views import home_view, product_view, item_view, product_detail_view, product_create_form
from .views import product_create_raw_form, dynamic_look_view, product_delete_view

app_name='products'

urlpatterns = [
    path('del/<int:id>/', product_delete_view, name ='obj_delete'),
    path('cfm/',product_create_raw_form, name='form_type'),
    path('product/', product_view, name='prod'),
    path('product_detail/', product_detail_view, name ='detail'),
    path('cmm/', product_create_form, name='model_type'),
    path('cmm/<int:id>/', dynamic_look_view , name ='dyanmic-routing'),
    path('item/', item_view),
]
