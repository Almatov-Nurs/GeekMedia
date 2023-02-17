# Generated by Django 4.1.6 on 2023-02-17 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(null=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='posts.posts')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]