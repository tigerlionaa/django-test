from django.urls import path, include
from customers import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('subscriptions/',  views.SubscriptionList.as_view()),
    path('subscription/<int:pk>/', views.SubscriptionDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)