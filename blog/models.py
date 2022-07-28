from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Fake"), (1, "Fact"))

class Post(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories')
    created = models.DateTimeField(auto_now_add=True)
    fake = models.ManyToManyField(User, related_name='post_fake', blank=True)
    fact = models.ManyToManyField(User, related_name='post_fact', blank=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Message(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="messages")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_messages')
    body = models.TextField()
    received = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-received"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"