from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

app_name = 'notices'

urlpatterns = [
	path('',views.home,name='home'),
	path('notice/<int:notice_id>',views.notice,name='notice'),
	path('category/<int:cat_id>',views.category,name='category'),
	path('aboutus',views.aboutus,name='aboutus'),
	path('contactus',views.contactus,name='contactus'),
	path('api/',include(router.urls)),


]