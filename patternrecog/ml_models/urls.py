from django.urls import path
from .views import PredictModelView

urlpatterns = [
    path('predict/', PredictModelView.as_view(), name='predict'),
]

app_name = 'ml_models'