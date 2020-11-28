from django.db import models

# a model is a class that represents a table in our database
# every attribute of the class is a field(column) of the table
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # upload_to specifies the directory where the image will be uploaded to 
    image = models.ImageField(upload_to='portfolio_app/images/')
    url = models.URLField(blank=True)
