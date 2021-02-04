from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from ESEA_core import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('organisations/', views.OrganisationList.as_view()),
    path('organisations/<int:pk>/', views.OrganisationDetail.as_view()),
    path('subscriptions/', views.SubscriptionList.as_view()),
    path('subscriptions/<int:pk>/', views.SubscriptionDetail.as_view())
]