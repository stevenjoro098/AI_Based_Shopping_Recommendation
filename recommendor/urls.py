from django.urls import path
from .views import get_recommendations, save_user_preferences

urlpatterns = [
    path('', get_recommendations, name='recommend'),
    path('save-preferences/', save_user_preferences)
]