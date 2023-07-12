from django.urls import path
from . import views

app_name = "api_accounts"

urlpatterns = [
    path("accounts/sign-up/", views.SignUp.as_view(), name="sign-up"),
    path("accounts/<uuid:pk>/", views.UserDetail.as_view(), name="user-rud")
]
