from django.db import models

# Create your models here.
class Expenses(models.Model):
    book_id = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100)
    # add float field for distribution_expense with 2 decimal places
    distribution_expense = models.FloatField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "expenses"
