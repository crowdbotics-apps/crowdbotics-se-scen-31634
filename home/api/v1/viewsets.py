from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet, ReadOnlyModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import  permissions
from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
    PlanSerializer,
    AppSerializer,
    SubscriptionSerializer
)

from home.models import Plan, App, Subscription

class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})

class PlanViewSet(ReadOnlyModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = (permissions.IsAuthenticated, )


class AppViewSet(ModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ["get", "post", "put", "patch", ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(app__user=self.request.user)