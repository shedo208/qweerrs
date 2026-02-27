from django.db import models

class Category(models.Model):
    name = models.CharField("Категория ", max_length=100)
     
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Тема новостей", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    content = models.TextField("Описание новостей")
    image_url = models.CharField("Ссылка на URL фотку", max_length=500)
    created_at = models.DateTimeField("Время и дата публикации", auto_now_add=True)

    def __str__(self):
        return self.title

class Adv(models.Model):
    name = models.CharField("Компания", max_length=255, default="Company name")
    image_url = models.CharField("URL ссылка", max_length=500)

    def __str__(self):
        return self.name