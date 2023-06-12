from django.db import models
from django_extensions.db.fields import AutoSlugField


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='Multiple_image')

    

class Amenities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="amenities")
    
    def __str__(self):
        return self.name
    

class Property(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenities, related_name='residential_amenities')
    PROPERTY_TYPECHOICES = [
        ('R', 'RESIDENTIAL'),
        ('C', 'COMMERCIAL'),
    ]
    property_type= models.CharField(max_length=1, choices=PROPERTY_TYPECHOICES)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    area_min = models.IntegerField()
    area_max = models.IntegerField()
    price_min = models.IntegerField()
    price_max = models.IntegerField()
    psf = models.IntegerField("Per Sq. Ft")
    status = [
        ('U', 'UNDER_CONSTRUCTION'),
        ('N', 'NEW_LUNCH'),
        ('R', 'READY_MOVE'),
    ]
    status = models.CharField(max_length=1, choices=status)
    image = models.ManyToManyField(Image, related_name='Residential_image')
    rating = models.IntegerField()
    title_overview = models.CharField(max_length=200)
    title_one = models.CharField(max_length=100)
    dis_one = models.TextField()
    title_two = models.CharField(max_length=100)
    dis_two = models.TextField()
    title_three = models.CharField(max_length=100)
    dis_three = models.TextField()
    title_four = models.CharField(max_length=255)
    dis_four = models.TextField()
    description_overview = models.TextField()
    slug = AutoSlugField(populate_from=['title'], null=True, blank=True)


    def __str__(self):
        return self.title
    
    def get_rating_stars(self):
        return list(range(self.rating))


class Contact(models.Model):
    name = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    city = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name