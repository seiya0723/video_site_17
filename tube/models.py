from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator

import uuid


class Category(models.Model):

    class Meta:
        db_table = "category"

    # TIPS:数値型の主キーではPostgreSQLなど一部のDBでエラーを起こす。それだけでなく予測がされやすく衝突しやすいので、UUID型の主キーに仕立てる。
    id     = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False )
    name   = models.CharField(verbose_name="カテゴリー名", max_length=20)

    def __str__(self):
        return self.name


class Video(models.Model):

    class Meta:

        db_table = "video"

    id       = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False )
    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.PROTECT,related_name='video')
    dt       = models.DateTimeField(verbose_name="投稿日", default=timezone.now)

    title        = models.CharField(verbose_name="タイトル", max_length=50)
    description  = models.CharField(verbose_name="動画説明文", max_length=300)
    movie        = models.FileField(verbose_name="動画", upload_to="tube/movie", blank=True)
    thumbnail    = models.ImageField(verbose_name="サムネイル", upload_to="tube/thumbnail/", null=True)
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    edited       = models.BooleanField(default=False)

    views        = models.IntegerField(verbose_name="再生回数", default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title


class VideoComment(models.Model):

    class Meta:
        db_table = "video_comment"

    id      = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False )
    content = models.CharField(verbose_name="コメント文", max_length=500)
    target  = models.ForeignKey(Video, verbose_name="コメント先の動画", on_delete=models.CASCADE)
    dt      = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    def __str__(self):
        return self.content


#コメントに対するリプライのモデル
class VideoCommentReply(models.Model):

    class Meta:
        db_table = "video_comment_reply"

    id      = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False )
    content = models.CharField(verbose_name="リプライ", max_length=500)
    target  = models.ForeignKey(VideoComment, verbose_name="リプライ対象のコメント", on_delete=models.CASCADE)
    dt      = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    def __str__(self):
        return self.content



#コメントに対するリプライのモデル
class VideoCommentReplyToReply(models.Model):

    class Meta:
        db_table = "video_comment_reply_to_reply"

    id      = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False )
    content = models.CharField(verbose_name="動画コメントのリプライに対するリプライ", max_length=500)
    target  = models.ForeignKey(VideoCommentReply, verbose_name="リプライ対象のコメント", on_delete=models.CASCADE)
    dt      = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class History(models.Model):

    class Meta:
        db_table     = "history"

    id     = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    dt     = models.DateTimeField(verbose_name="視聴日時", default=timezone.now)
    target = models.ForeignKey(Video, verbose_name="視聴した動画", on_delete=models.CASCADE)
    user   = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="視聴したユーザー", on_delete=models.CASCADE)
    views  = models.IntegerField(verbose_name="視聴回数", default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.target.title


class MyList(models.Model):

    class Meta:
        db_table    = "mylist"

    id       = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    dt       = models.DateTimeField(verbose_name="登録日時", default=timezone.now)
    target   = models.ForeignKey(Video, verbose_name="マイリスト動画", on_delete=models.CASCADE)
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="登録したユーザー", on_delete=models.CASCADE)

    def __str__(self):
        return self.target.title


class Notify(models.Model):

    class Meta:
        db_table     = "notify"

    id      = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    dt      = models.DateTimeField(verbose_name="通知日時", default=timezone.now)
    content = models.CharField(verbose_name="通知内容", max_length=200)

    def __str__(self):
        return self.content


class GoodVideo(models.Model):

    class Meta:
        db_table    = "good_video"

    id      = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    dt      = models.DateTimeField(verbose_name="評価日時", default=timezone.now)
    target  = models.ForeignKey(Video, verbose_name="対象動画", on_delete=models.CASCADE, related_name="favorite")
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="高評価したユーザー", on_delete=models.CASCADE, related_name="favorite_from_user")

    def __str__(self):
        return self.target.title


#Reportモデルクラス
"""
class Report(models.Model):

    class Meta:
        db_table    = "report"

    id          = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    dt          = models.DateTimeField(verbose_name="評価日時", default=timezone.now)
    from_user   = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="通報したユーザー", on_delete=models.CASCADE)
    to_user     = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="通報されたユーザー", on_delete=models.CASCADE)
    reason      = models.CharField(verbose_name="通報理由", max_length=200)

"""


#Twitterのモデル(推測)
"""
    id          = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    dt          = models.DateTimeField(verbose_name="評価日時", default=timezone.now)
    target      = models.UUIDField(verbose_name="リプライ先",null=True,blank=True)
    content     = models.CharField(verbose_name="通知内容", max_length=200)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="高評価したユーザー", on_delete=models.CASCADE, related_name="favorite_from_user")

"""

