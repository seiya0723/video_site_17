# Generated by Django 3.2.5 on 2021-07-15 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_videocommentreply'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='videocomment',
            table='video_comment',
        ),
        migrations.AlterModelTable(
            name='videocommentreply',
            table='video_comment_reply',
        ),
    ]
