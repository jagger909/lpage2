from django.db import models

# Create your models here.



class Zayavka(models.Model):
    zayavka_text = models.CharField(max_length=200)
    telephon_number = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.zayavka_text
