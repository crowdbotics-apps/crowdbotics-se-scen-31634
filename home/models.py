from django.db import models
from django.conf import settings

class DateTimeModel(models.Model):
    """
        Abstract base model for created_at and updated_at fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Plan(DateTimeModel):
    """
        Model for pricing plans
    """
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField()

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"
        constraints =[models.CheckConstraint(check=models.Q(price__gte=0), name="price_greater_than_or_zero")]

    def __str__(self):
        return self.name


class App(DateTimeModel):
    """
        Model for details of metadata of app
    """
    TYPE_CHOICES = (
        ("Web", "Web"),
        ("Mobile", "Mobile"),
    )

    FRAMEWORK_CHOICES = (
        ("Django", "Django"),
        ("React Native", "React Native"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="apps")
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    framework = models.CharField(max_length=100, choices=FRAMEWORK_CHOICES)
    domain_name = models.CharField(max_length=100, null=True, blank=True)
    screenshot = models.ImageField(upload_to="screenshots", null=True, blank=True)

    class Meta:
        verbose_name = "App"
        verbose_name_plural = "Apps"
        constraints=[models.UniqueConstraint(fields=["user", "name"], name="unique_app_name_for_user")]

    def __str__(self):
        return self.name


class Subscription(DateTimeModel):
    """
        Model for plan associated with particular app
    """
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="subscriptions")
    app = models.OneToOneField(App, on_delete=models.CASCADE)
    active = models.BooleanField()

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return f"{self.app} / {self.plan}"
