from django.db import models

# Create your models here.
class Bali_Offer(models.Model):
    #bali_offer_id = models.IntegerField(primary_key=True)
    bali_offer_date = models.DateField(auto_now=False)
    bali_offer_text = models.CharField(max_length=50)
    bali_offer_featured = models.BooleanField(default=False)


class Carol_Image(models.Model):
    CATEGORY_OPTIONS = {
    ('TeakWood','TeakWood'),
    ('Antique', 'Antique'),
    ('Gift','Gift'),
    }
    #carol_image_id = models.IntegerField(primary_key=True)
    carom_image_date = models.DateField(auto_now=False)
    carol_image_category1 = models.CharField(max_length=20,choices=CATEGORY_OPTIONS, default='TeakWood')
    carol_image_desc1 = models.CharField(max_length=30)
    carol_image_loc1 = models.ImageField(upload_to='%Y/%m', null=True, blank=True)
    carol_image_category2 = models.CharField(max_length=20,choices=CATEGORY_OPTIONS,
    default='Antique')
    carol_image_desc2 = models.CharField(max_length=30)
    carol_image_loc2 = models.ImageField(upload_to='%Y/%m', null=True, blank=True)
    carol_image_category3 = models.CharField(max_length=20,choices=CATEGORY_OPTIONS,default='Gift')
    carol_image_desc3 = models.CharField(max_length=30)
    carol_image_loc3 = models.ImageField(upload_to='%Y/%m', null=True, blank=True)
    carol_image_featured = models.BooleanField(default=False)
