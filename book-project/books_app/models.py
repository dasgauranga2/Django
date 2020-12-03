from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

class Book(models.Model):
    # update the 'id' field of the model to be a UUID field
    # set it as the primary key
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.title
    
    # tell django how to calculate the representative URL for the object
    # this method should return a string that can be used to refer to the object over HTTP
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
    # foreign-key field that links 'Book' model to 'Review' model
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review = models.CharField(max_length=300)
    # foreign-key field that links the custom user model to 'Review' model
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.review
