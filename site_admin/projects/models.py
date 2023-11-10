from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to='images')
    description_short = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
