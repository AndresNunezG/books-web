from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, null=True)
    author_name = models.CharField(max_length=50, null=True)
    action_adventure = 'AA'
    classics = 'CL'
    comic = 'CM'
    detective_mystery = 'DM'
    fantasy = 'FT'
    category_choices = [
        (action_adventure,'Action and Adventure'),
        (classics, 'Classics'),
        (comic, 'Comic Book'),
        (detective_mystery, 'Detective and Mystery'),
        (fantasy, 'Fantasy'),
    ]
    category = models.CharField(
        max_length=2,
        choices=category_choices,
        default=classics,
        )
    isbn = models.CharField(max_length=13, null=True)
    publication_date = models.DateField(max_length=20, default=timezone.now())
