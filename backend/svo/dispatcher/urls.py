from rest_framework import routers

from dispatcher import views

router = routers.SimpleRouter()

router.register(r"applications", views.ApplicationViewSet)

urlpatterns = [

]
urlpatterns += router.urls
