import factory
from factory.django import DjangoModelFactory
from faker import Factory
from users.models import User
from home.models import Plan, App, Subscription

faker = Factory.create()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = faker.name()
    email = faker.email()


class PlanFactory(DjangoModelFactory):
    class Meta:
        model = Plan

    name = "Free"
    price = 0.00
    description = factory.lazy_attribute(lambda obj: f'This is {obj.name} plan for price {obj.price}.')


class AppFactory(DjangoModelFactory):
    class Meta:
        model = App

    name = factory.Faker('word')
    description = factory.Faker('text')
    domain_name = factory.Faker('url')
    screenshot = factory.django.ImageField()
    user = factory.SubFactory(UserFactory)


class SubscriptionFactory(DjangoModelFactory):
    class Meta:
        model = Subscription

    app = factory.SubFactory(AppFactory)
    plan = factory.SubFactory(PlanFactory)
    active = True