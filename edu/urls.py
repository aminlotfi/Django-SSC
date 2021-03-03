from django.urls import path
from .views import Index, SignUp, SignIn

urlpatterns = [
    path('index/', Index.as_view(), name="index"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('signin/', SignIn.as_view(), name="signin")

]