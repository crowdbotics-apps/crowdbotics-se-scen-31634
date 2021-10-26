import pytest
from pytest_factoryboy import register
from home.tests.factories import UserFactory, PlanFactory, AppFactory, SubscriptionFactory


register(UserFactory)
register(PlanFactory)
register(AppFactory)
register(SubscriptionFactory)


@pytest.fixture
def authenticated_client(client, django_user_model):
    USERNAME = "crowdboticstestuser"
    PASSWORD = "abc@54321"
    django_user_model.objects.create_user(username=USERNAME, password=PASSWORD)
    client.login(username=USERNAME, password=PASSWORD)
    return client

@pytest.fixture
def free_plan():
    return PlanFactory(name="Free", price=0.00)

@pytest.fixture
def standard_plan():
    return PlanFactory(name="Standard", price=10.00)

@pytest.fixture
def pro_plan():
    return PlanFactory(name="Pro", price=25.00)

@pytest.fixture
def django_web_app():
    return AppFactory(type="Web", framework="Django")

@pytest.fixture
def react_native_mobile_app():
    return AppFactory(type="Mobile", framework="React Native")

@pytest.fixture
def subscription():
    return SubscriptionFactory()