from django.urls import path
from . import views

app_name = "notifications"
urlpatterns = [
    path("", view=views.Notifications.as_view(), name="Notifications"),
   ]
