import os
import csv
# import openpyxl
from django.core.management.base import BaseCommand
from dashboard.models import Expenses

class Command(BaseCommand):
    help = 'Load a list of books from an Excel file into the database'

    def handle(self, *args, **kwargs):
        path = os.path.join('static', 'books.csv')  # Adjust the path to your static directory as needed
        
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
        
        for row in reader:
            Expenses.objects.create(
                book_id=row[0],
                title=row[1],
                subtitle=row[2],
                authors=row[3],
                publisher=row[4],
                published_date=row[5],
                category=row[6],
                distribution_expense=row[7],
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
