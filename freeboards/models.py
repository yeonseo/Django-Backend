from django.utils import timezone
from django.db import models
from django.urls import reverse
from core import models as core_models
# from cal import Calendar

class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BoardType(AbstractItem):
    """ BoardType Model Definition """

    class Meta:
        verbose_name_plural = "3. 게시물 분류 관리"


class Comment(core_models.TimeStampedModel):
    """ Comment Model Definition """

    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    username = models.ForeignKey('users.User', related_name="comments", on_delete=models.CASCADE)
    board = models.ForeignKey('freeboards.FreeBoard', related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.username} says: {self.comment}"

    class Meta:
        verbose_name_plural = "2. 댓글 관리"

class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="board_photos")
    image = models.ForeignKey("FreeBoard", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption



class FreeBoard(core_models.TimeStampedModel):
    """ Custom FreeBoard Model """
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)  # 게시물 제목
    content = models.TextField()  # 게시물 내용
    username = models.ForeignKey('users.User', related_name="boards", on_delete=models.CASCADE)  # 게시물 작성자
    views = models.IntegerField(default=0)  # 게시물 조회수
    files = models.FileField(max_length=100, null=True, blank=True)  # 게시물 첨부파일
    board_type = models.ManyToManyField('BoardType', blank=True)  #게시물 타입
    comment = models.ManyToManyField('Comment', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "1. 게시물 관리"