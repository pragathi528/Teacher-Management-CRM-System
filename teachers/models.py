from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=50,unique=True)
    image = models.ImageField(upload_to="teachers/", blank=True, null=True)

    class Meta:
        verbose_name = "Teacher"

    def __str__(self):
        return (f"{self.name} - {self.subject}")