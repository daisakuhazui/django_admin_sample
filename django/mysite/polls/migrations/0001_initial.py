# Generated by Django 2.1.1 on 2018-09-24 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('brires', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Series'),
        ),
    ]
