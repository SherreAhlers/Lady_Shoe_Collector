from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
CLEANINGS = (
    ('D', 'Deep Cleaning'),
    ('W', 'Wipe Down'),
    ('RS', 'Re-Soled'),
)

class Outfit(models.Model):
    top = models.CharField(max_length=50)
    bottom = models.CharField(max_length=50)

    def __str__(self):
        return self.top

    def get_absolute_url(self):
        return reverse('outfits_detail', kwargs={'pk': self.id})

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    shoe_type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    outfits = models.ManyToManyField(Outfit)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})

    def cleaned_after_use(self):
        return self.cleaning_set.filter(date=date.today()).count() >= len(CLEANINGS)

class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    cleaning_type = models.CharField(
        max_length=2, 
        choices=CLEANINGS,
        default=CLEANINGS[0][0]
        )
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_cleaning_type_display()} on {self.date}"

    class Meta: 
        ordering = ['-date']