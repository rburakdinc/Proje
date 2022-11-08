from tabnanny import verbose
from django.db import models

class Hayvan(models.Model):
    name = models.CharField(max_length=50,verbose_name='Hayvan Adı:')
    description = models.TextField(verbose_name='Açıklama')
    image = models.CharField(max_length=25,verbose_name='Hayvan Resmi:')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Aramıza Katılma Tarihi')
    isAvailable = models.BooleanField(default =True)
    
    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/' + self.image