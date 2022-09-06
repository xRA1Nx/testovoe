from django.db import models


class Color(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class AutoModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AutoMark(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(AutoModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    model = models.ForeignKey(AutoModel, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField(auto_now=True)
