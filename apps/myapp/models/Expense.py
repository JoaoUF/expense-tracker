from utils.model import Model
from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Expense(ActivatorModel, TimeStampedModel, Model):
    name = models.CharField(
        db_column='name',
        max_length=100,
    )
    amount = models.IntegerField(
        db_column='amount'
    )
    category = models.CharField(
        max_length=50,
        db_column='category',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MAE_EXPENSE'
