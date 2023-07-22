from django.db import models

# Create your models here.

   

class Cast(models.Model):
    name = models.CharField(default="Name Not Available", max_length=1000)
    credits = models.CharField(default="Credits not available", max_length=1000)
    title = models.CharField(default="Title not available", max_length=1000)
    character_name = models.CharField(default="Character Name not available", max_length=1000)
    img = models.TextField(default="https://westsiderc.org/wp-content/uploads/2019/08/Image-Not-Available.png")

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(default="Title not available", max_length=1000)
    media_type = models.CharField(default="Media type not available", max_length=1000)
    year = models.IntegerField()
    genre = models.CharField(default="Genre not available", max_length=1000)
    duration = models.IntegerField()
    disabilities = models.CharField(default="Disabilities not available", max_length=1000)
    cast_members = models.ManyToManyField(Cast)
    themes = models.CharField(max_length=1000)
    img = models.TextField(default="https://westsiderc.org/wp-content/uploads/2019/08/Image-Not-Available.png")
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(default="No Title", max_length=1000)
    reviewer_name = models.CharField(default="Anonymous", max_length=1000)
    review_text = models.TextField(default="Review Text Not Available", max_length=1000)
    date = models.CharField(default="No Date Added", max_length=1000)
    casting_score = models.FloatField()
    character_score = models.FloatField()
    originality_score = models.FloatField()
    accuracy_score = models.FloatField()

    def __str__(self):
        return self.reviewer_name



