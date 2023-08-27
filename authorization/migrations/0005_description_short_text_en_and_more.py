# Generated by Django 4.2.3 on 2023-08-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_globalactive_check_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='short_text_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок описания EN'),
        ),
        migrations.AddField(
            model_name='description',
            name='short_text_instruction',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок описания инструкции'),
        ),
        migrations.AddField(
            model_name='description',
            name='short_text_instruction_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок описания инструкции EN'),
        ),
        migrations.AddField(
            model_name='description',
            name='text_app_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание EN'),
        ),
        migrations.AddField(
            model_name='description',
            name='text_instruction',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Инструкции'),
        ),
        migrations.AddField(
            model_name='description',
            name='text_instruction_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Инструкции EN'),
        ),
    ]
