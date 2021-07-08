from django.urls import path
from . import views
app_name='qwe'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('shop/<int:book_id>',views.detail,name='detail'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:ji_id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]