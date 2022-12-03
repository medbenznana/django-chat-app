from django.contrib.auth.models import User
from django.db import models

__author__ = 'BENZNANA Mohamed : benznana.med@gmail.com'


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return "@%s says : (%s) ON : -%s- room" % (self.user, self.content[:50], self.room.name, )
