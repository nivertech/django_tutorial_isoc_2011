from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

