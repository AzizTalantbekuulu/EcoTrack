from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['role']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # добавляем related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # добавляем related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='user',
    )


class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=50)


class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    co2 = models.FloatField()


class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, related_name='alerts', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
