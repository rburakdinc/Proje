# Generated by Django 4.0.3 on 2022-04-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hayvanlar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hayvan',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hayvan',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Aramıza Katılma Tarihi'),
        ),
        migrations.AlterField(
            model_name='hayvan',
            name='description',
            field=models.TextField(verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='hayvan',
            name='image',
            field=models.CharField(max_length=25, verbose_name='Hayvan Resmi:'),
        ),
        migrations.AlterField(
            model_name='hayvan',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Hayvan Adı:'),
        ),
    ]
