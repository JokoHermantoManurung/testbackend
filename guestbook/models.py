from django.db import models

# Create your models here.
class GuestBook(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nama