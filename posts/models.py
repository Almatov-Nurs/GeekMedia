from django.core.validators import FileExtensionValidator
from django.db import models


class Category(models.Model):
    ru_title = models.CharField(max_length=100)
    en_title = models.CharField(max_length=100)

    def __str__(self):
        return self.en_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Posts(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_date = models.DateField(null=True)
    created_date_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"{' '.join(self.title.split(' ')[0:4])}..."

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Articles(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="articles", null=True)

    def __str__(self):
        return f"{self.post}: {self.title}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class MultiMedia(models.Model):
    title = models.CharField(max_length=100)
    media = models.FileField(upload_to='videos_uploaded', validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мультимедиа"
        verbose_name_plural = "Мультимедии"
