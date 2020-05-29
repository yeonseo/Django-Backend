from django.db import models
from core import models as core_models

class Movie(core_models.TimeStampedModel):
    title = models.CharField(max_length=30)  # 제목
    genre = models.CharField(max_length=15)  # 장르
    year = models.IntegerField()  # 제작 년도

    def __str__(self):
        return self.title
