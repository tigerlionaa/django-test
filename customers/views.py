from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customers.models import SubscriptionInfo
from customers.serializers import UserSerializer, SubscriptionInfoSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from customers.permissions import IsSubscriberOrReadOnly

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
    Using Generic Class-Based Views the below two views are trim down into super concise
    and DRY principled way.
    We can see the exact two views are also defined below, commented out, using Function-Based Views
'''
class SubscriptionList(generics.ListCreateAPIView):
    queryset = SubscriptionInfo.objects.all()
    serializer_class = SubscriptionInfoSerializer

    '''
        'IsAuthenticatedOrReadOnly' ensures that authenticated requests get read-write access, 
        and unauthenticated requests get read-only access.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overriding .perform_create() method to represent individual subscriber instance
    def perform_create(self, serializer):
        serializer.save(subscriber=self.request.user)

class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionInfo.objects.all()
    serializer_class = SubscriptionInfoSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                            IsSubscriberOrReadOnly]



