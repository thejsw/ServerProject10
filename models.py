# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class History(models.Model):
    date = models.DateField(primary_key=True)
    sheetcnt = models.SmallIntegerField(db_column='sheetCnt', blank=True, null=True)  # Field name made lowercase.
    wrongcnt = models.SmallIntegerField(db_column='wrongCnt', blank=True, null=True)  # Field name made lowercase.
    email = models.ForeignKey('Info', models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'history'


class Info(models.Model):
    email = models.CharField(primary_key=True, max_length=40)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'info'


class Note(models.Model):
    seq = models.IntegerField(primary_key=True)
    date = models.DateField()
    memo = models.CharField(max_length=500, blank=True, null=True)
    word = models.ForeignKey('Worksheet', models.DO_NOTHING, db_column='word', db_comment='workcheet 외래키')
    email = models.ForeignKey(Info, models.DO_NOTHING, db_column='email', db_comment='userInfo 외래키')

    class Meta:
        managed = False
        db_table = 'note'


class Worksheet(models.Model):
    word = models.CharField(primary_key=True, max_length=40)
    image = models.CharField(max_length=500, blank=True, null=True)
    meaning = models.CharField(max_length=100)
    subject = models.IntegerField(db_comment='1,2,3')

    class Meta:
        managed = False
        db_table = 'worksheet'
