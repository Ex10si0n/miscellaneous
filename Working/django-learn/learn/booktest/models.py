from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    
    # Override super class methods
    
    def create_book(self, bTitle, bPub_date):
        obj = BookInfo()
        obj.bTitle = bTitle
        obj.bPub_date = bPub_date
        obj.save()
        return obj

class BookInfo(models.Model):
    '''
    ORM Class - Relation to Database
    Book Model Class
    Must Inheritent models.Model
    '''
    bTitle = models.CharField(max_length=20)  # CharField 字符串
    bPub_date = models.DateField()            # DateField 日期
    objects = BookInfoManager()               # BookInfo Manager Object 管理器对象 -> 用于封装增删改查方法

    def __str__(self):
        return self.bTitle                    # Make Admin Page Shows BookTitle

    # class Meta:
    #     db_table = 'bookInfo'                 # Model Class 对应的表名不依赖于应用名字
    

# 1 to * mapping from BookInfo to Character
class Character(models.Model):
    '''
    ORM Class
    Character Model Class
    Must Inheritent models.Model
    Implementing Relational Database
    '''
    hName = models.CharField(max_length=20)
    hGender = models.BooleanField(default=False)  # BooleanField 布尔值
    hComment = models.CharField(max_length=128)
    hBook = models.ForeignKey('BookInfo', on_delete=models.CASCADE) # ForeignKey to BookInfo.id
    
    def __str__(self):
        return self.hName                         # Make Admin Page Shows BookTitle
