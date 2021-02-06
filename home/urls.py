from .views import *
from django.urls import path

urlpatterns = [
    path('level-1',level1,name='level1'),
    path('level-2',level2,name='level1'),
    path('level-6',level6,name='level1'),
    path('shop-page',shop,name='shop')
    ]