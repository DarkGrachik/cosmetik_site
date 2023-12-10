from django.db import models

class Cosmetiks(models.Model):
    cosm_id = models.AutoField(primary_key=True)
    cosm_name = models.CharField(max_length=100)
    cosm_description = models.CharField(max_length=1000, blank=True, null=True)
    cosm_status = models.CharField(max_length=100)
    date_of_creation = models.DateField()
    date_of_publication = models.DateField(blank=True, null=True)
    date_of_close = models.DateField(blank=True, null=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='owner')
    moderator = models.ForeignKey('Users', models.DO_NOTHING, db_column='moderator', related_name='cosmetiks_moderator_set')

    class Meta:
        managed = False
        db_table = 'cosmetiks'
        app_label = 'cosmetik_lab3'

class SubCosm(models.Model):
    sub = models.ForeignKey('Substanses', models.DO_NOTHING)
    cosm = models.ForeignKey(Cosmetiks, models.DO_NOTHING)
    percent_in = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sub_cosm'
        app_label = 'cosmetik_lab3'

class Substanses(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=100)
    sub_description = models.CharField(max_length=1000)
    sub_status = models.BooleanField(blank=True, null=True)
    sub_short_descr = models.CharField(max_length=150, blank=True, null=True)
    image2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'substanses'
        app_label = 'cosmetik_lab3'


class Test(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    access = models.BooleanField()
    

    class Meta:
        managed = False
        db_table = 'users'
        app_label = 'cosmetik_lab3'
