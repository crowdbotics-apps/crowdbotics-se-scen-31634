from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    PlanViewSet,
    AppViewSet,
    SubscriptionViewSet
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("plan", PlanViewSet, basename="plan")
router.register("app", AppViewSet, basename="app")
router.register("subscription", SubscriptionViewSet, basename="subscription")

urlpatterns = [
    path("", include(router.urls)),
]
