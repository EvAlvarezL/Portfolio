# Generated by Django 4.0 on 2022-11-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyectos',
            options={'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AddField(
            model_name='proyectos',
            name='imagen',
            field=models.ImageField(default='DEFAULT VALUE', upload_to=''),
        ),
    ]