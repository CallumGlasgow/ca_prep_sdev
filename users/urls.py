from django.urls import path
from .views import SignUpView, HomePageView, LoginView


urlpatterns = [
   # path('login/', LoginView.as_view(), name='login'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]