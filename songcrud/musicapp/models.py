from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Song(models.Model):
    title = models.CharField(max_length=400)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField(default=0)
    artist_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content