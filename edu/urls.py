from django.urls import path
from .views import Index, Register, Login, logout_user

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('register/', Register.as_view(), name="registration"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout_user, name="logout")
]
