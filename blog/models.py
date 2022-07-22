from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Fake"), (1, "Fact"))

class Post(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=300, unique=True)
    status = models.IntegerField(choices=STATUS)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories')
    created = models.DateTimeField(auto_now_add=True)
    fake = models.ManyToManyField(User, related_name='post_fake', blank=True)
    fact = models.ManyToManyField(User, related_name='post_fact', blank=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def number_of_fake(self):
        return self.fake.count()

    def number_of_fact(self):
        return self.fact.count()
