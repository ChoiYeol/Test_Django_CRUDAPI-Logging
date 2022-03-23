from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다

class User(AbstractUser): pass


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    countryCode = models.CharField(db_column='CountryCode', max_length=35)  # Field name made lowercase.
    # countrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryCode')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'

class Post(models.Model):
    postname = models.CharField(max_length=50)

    #게시글 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    
    contents = models.TextField()

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname
