import pytest
from django.urls import  reverse
from rest_framework import status
from home.api.v1.serializers import AppSerializer, SubscriptionSerializer

pytestmark = pytest.mark.django_db

class TestUnAuthenticatedPlanViewSet:
    def test_plan_list_view(self, client):
        url = reverse('plan-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_free_plan_detail_view(self, client, free_plan):
        url = reverse('plan-detail', args=[free_plan.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_standard_plan_detail_view(self, client, standard_plan):
        url = reverse('plan-detail', args=[standard_plan.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_pro_plan_detail_view(self, client, pro_plan):
        url = reverse('plan-detail', args=[pro_plan.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

class TestAuthenticatedPlanViewSet:
    def test_plan_list_view(self, authenticated_client):
        url = reverse('plan-list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_free_plan_detail_view(self, authenticated_client, free_plan):
        url = reverse('plan-detail', args=[free_plan.id])
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_standard_plan_detail_view(self, authenticated_client, standard_plan):
        url = reverse('plan-detail', args=[standard_plan.id])
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_pro_plan_detail_view(self, authenticated_client, pro_plan):
        url = reverse('plan-detail', args=[pro_plan.id])
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK

class TestUnAuthenticatedAppViewSet:
    def test_app_list_view(self, client):
        url = reverse('app-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_django_web_app_detail_view(self, client, django_web_app):
        url = reverse('app-detail', args=[django_web_app.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_react_native_mobile_app_detail_view(self, client, react_native_mobile_app):
        url = reverse('app-detail', args=[react_native_mobile_app.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_django_web_app_create_view(self, client, django_web_app):
        url = reverse('app-list')
        data = AppSerializer(django_web_app).data
        data.pop("user")
        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_react_native_mobile_app_create_view(self, client, react_native_mobile_app):
        url = reverse('app-list')
        data = AppSerializer(react_native_mobile_app).data
        data.pop("user")
        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

class TestAuthenticatedAppViewSet:
    FORMAT = "multipart/form-data"
    def test_app_list_view(self, authenticated_client):
        url = reverse('app-list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_django_web_app_create_view(self, authenticated_client, django_web_app):
        url = reverse('app-list')
        data = AppSerializer(django_web_app).data
        screenshot = data.pop("screenshot")
        with open(screenshot, "rb") as screenshotfile:
            data["screenshot"] = screenshotfile
            response = authenticated_client.post(url, data=data, format=self.FORMAT)
            assert response.status_code == status.HTTP_201_CREATED

    def test_react_native_mobile_app_create_view(self, authenticated_client, react_native_mobile_app):
        url = reverse('app-list')
        data = AppSerializer(react_native_mobile_app).data
        screenshot = data.pop("screenshot")
        with open(screenshot, "rb") as screenshotfile:
            data["screenshot"] = screenshotfile
            response = authenticated_client.post(url, data=data, format=self.FORMAT)
            assert response.status_code == status.HTTP_201_CREATED

class TestUnAuthenticatedSubscriptionViewSet:
    def test_subscription_list_view(self, client):
        url = reverse('subscription-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_subscription_detail_view(self, client, subscription):
        url = reverse('subscription-detail', args=[subscription.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_subscription_create_view(self, client, subscription):
        url = reverse('subscription-list')
        data = SubscriptionSerializer(subscription).data
        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

class TestAuthenticatedSubscriptionViewSet:
    def test_subscription_list_view(self, authenticated_client):
        url = reverse('app-list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK