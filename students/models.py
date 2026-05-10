from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=10, unique=True)
    student_branch = models.CharField(max_length=50)
    student_contact = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='students/', null=True, blank=True)

    class Meta:
        verbose_name = "Student"

    def __str__(self):
        return self.student_name
