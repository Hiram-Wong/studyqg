from django.db import models


# Create your models here.

class QuestionLib(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField(verbose_name="题目")
    answer = models.CharField(max_length=255, verbose_name="答案")
    A = models.TextField(verbose_name="选项A")
    B = models.TextField(verbose_name="选项B")
    C = models.TextField(verbose_name="选项C", null=True)
    D = models.TextField(verbose_name="选项D", null=True)

    def __str__(self):
        return self.question


class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, default="image", verbose_name="类型")
    url = models.CharField(max_length=255, verbose_name="banner链接")

    def __str__(self):
        return str(self.id)


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    versation = models.CharField(max_length=255, verbose_name="版本号")
    time = models.DateField(verbose_name="时间")
    description = models.TextField(max_length=255, verbose_name="详情")

    def __str__(self):
        return self.versation


class Basic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="标题")

    def __str__(self):
        return self.title
