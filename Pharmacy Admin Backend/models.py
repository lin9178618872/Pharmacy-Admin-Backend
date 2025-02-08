from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
