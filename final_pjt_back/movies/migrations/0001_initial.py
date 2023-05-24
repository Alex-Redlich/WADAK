# Generated by Django 3.2.18 on 2023-05-24 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(null=True)),
                ('vote_average', models.FloatField()),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('tagline', models.CharField(max_length=100, null=True)),
                ('backdrop_path', models.CharField(max_length=200, null=True)),
                ('poster_path', models.CharField(max_length=200, null=True)),
                ('release_date', models.CharField(max_length=50, null=True)),
                ('runtime', models.CharField(max_length=30, null=True)),
                ('genres', models.ManyToManyField(related_name='gerne_movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_like_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='like_movies', through='movies.Movie_like_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
