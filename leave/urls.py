from django.urls import path
from .views import *

urlpatterns = [
    path('apply/', apply_leave,name='apply_leave'),
    path('my_leaves/',my_leaves, name='my_leaves'),
    path('view/', view_leaves,name='view_leaves'),
    path('approve/<int:id>',approve_leave,name='approve_leave'),
    path('reject/<int:id>',reject_leave, name='reject_leave')
    
    
    ]