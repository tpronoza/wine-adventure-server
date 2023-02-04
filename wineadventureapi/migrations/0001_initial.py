# Generated by Django 4.1.5 on 2023-02-04 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wine_name', models.CharField(max_length=100)),
                ('year_produced', models.CharField(max_length=50)),
                ('wine_picture', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('wine_type', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('favorite', models.BooleanField(default=False)),
                ('wish_list', models.BooleanField(default=False)),
                ('wine_list', models.BooleanField(default=False)),
                ('country_name', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wineadventureapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Wine_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wineadventureapi.category')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winecat', to='wineadventureapi.wine')),
            ],
        ),
        migrations.CreateModel(
            name='Wine101',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=50)),
                ('context', models.CharField(max_length=100)),
                ('article_image', models.CharField(max_length=100)),
                ('article_link', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wineadventureapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_image', models.CharField(max_length=1000)),
                ('about_me', models.CharField(max_length=1000)),
                ('favorite', models.CharField(max_length=1000)),
                ('wish_list', models.CharField(max_length=1000)),
                ('my_wines_list', models.CharField(max_length=1000)),
                ('uid', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wineadventureapi.user')),
            ],
        ),
    ]
