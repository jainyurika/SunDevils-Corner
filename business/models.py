from django.db import models

# Create your models here.

class BusinessCat(models.Model):
    class Meta:
        verbose_name_plural = "Business Categories"

    OPTIONS = [
        ('Grocery Store', 'Grocery Store'),
        ('Apartment', 'Apartment'),
        ('Haircut Shop', 'Haircut Shop'),
        ('Restaurants', 'Restaurants'),
    ]

    name = models.CharField(max_length=15, verbose_name="Category", choices=OPTIONS)
    
    def __str__(self):
        return self.name



class Business(models.Model):

    class Meta:
        verbose_name_plural = "Businesses"

    name = models.CharField(max_length=60, null=False, verbose_name="Title")
    about = models.TextField(max_length=5000, null=True, verbose_name="Description", blank=True)
    upvotecount = models.IntegerField(default=0, verbose_name="Upvote Count")
    phone = models.CharField(max_length=10, null=False, verbose_name="Contact Number")
    address = models.CharField(max_length=100, null=False, verbose_name="Address")
    website = models.CharField(max_length=100, null=False, verbose_name="Website")
    distfromcampus = models.FloatField(default=0, verbose_name="Distance from Campus")
    category = models.ForeignKey(BusinessCat, on_delete=models.CASCADE, verbose_name="Category", null=True, blank=True)

    def __str__(self):
        return self.name + " - " + self.category.name + " - " + str(self.upvotecount)