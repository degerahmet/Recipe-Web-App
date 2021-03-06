# Generated by Django 3.1 on 2020-09-09 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitiy', models.CharField(max_length=255)),
                ('measure', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('specialname', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('ingredients', models.ManyToManyField(blank=True, related_name='recipe', to='recipebook.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('direction', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='recipebook.recipe')),
            ],
        ),
    ]
