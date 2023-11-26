from django.db import models

# Create your models here.
class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_date = models.DateField()
    category = models.CharField(max_length=100)
    distribution_expense = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "expenses"
