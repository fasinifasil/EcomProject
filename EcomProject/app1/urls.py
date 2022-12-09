from django.contrib import admin
from django.urls import path,include
from app1 import views
app_name='app1'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodcatdetail'),



]