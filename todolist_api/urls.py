from django.urls import include, path
from rest_framework import routers

from todo import views



router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
