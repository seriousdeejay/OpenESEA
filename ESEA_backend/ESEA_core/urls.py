from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ESEA_core import views

urlpatterns = [
    path('subscriptions/', views.SubscriptionList.as_view()),
    path('subscriptions/<int:pk>/', views.SubscriptionDetail.as_view())
]