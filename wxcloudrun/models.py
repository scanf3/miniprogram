from datetime import datetime

from django.db import models

from wxcloudrun.common.constants import EntityStatus, EntityType
from wxcloudrun.common.utils import create_field_choices


# Create your models here.
# class Counters(models.Model):
#     id = models.AutoField
#     count = models.IntegerField(max_length=11, default=0)
#     createdAt = models.DateTimeField(default=datetime.now(), )
#     updatedAt = models.DateTimeField(default=datetime.now(), )
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         db_table = 'Counters'  # 数据库表名


class AuthUser(models.Model):
    id = models.AutoField
    open_id = models.CharField(max_length=60, default='')
    createdAt = models.DateTimeField(auto_now_add=True)


class Entity(models.Model):
    id = models.AutoField
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=create_field_choices(EntityStatus), default=EntityStatus.UNKNOWN)
    type = models.CharField(max_length=20, choices=create_field_choices(EntityType))
