# Generated by Django 4.0.5 on 2022-07-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pecas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprimento', models.FloatField()),
                ('largura', models.FloatField()),
                ('material', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sobras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprimento', models.FloatField()),
                ('largura', models.FloatField()),
                ('material', models.CharField(max_length=20)),
            ],
        ),
    ]