from django.db import models


class Description(models.Model):
    status_update = models.BooleanField(default=False)
    version_app = models.CharField(max_length=255, verbose_name="Версия приложения")
    short_text = models.CharField(max_length=255, verbose_name="Заголовок описания")
    short_text_en = models.CharField(max_length=255, verbose_name="Заголовок описания EN", blank=True, null=True)
    text_app = models.TextField(verbose_name="Описание")
    text_app_en = models.TextField(verbose_name="Описание EN", blank=True, null=True)

    short_text_instruction = models.CharField(max_length=255, verbose_name="Заголовок описания инструкции", blank=True, null=True)
    short_text_instruction_en = models.CharField(max_length=255, verbose_name="Заголовок описания инструкции EN", blank=True, null=True)

    text_instruction = models.TextField(verbose_name="Описание Инструкции", blank=True, null=True)
    text_instruction_en = models.TextField(verbose_name="Описание Инструкции EN", blank=True, null=True)

    def __str__(self):
        return self.short_text


class GlobalActive(models.Model):
    global_active = models.BooleanField(default=True)
    check_stat = models.BooleanField(default=True)


class Cmndr(models.Model):
    name_cmdr = models.CharField(max_length=255, verbose_name="Имя пользователя")
    code_active = models.CharField(max_length=255, verbose_name="Уникальный код", unique=True)
    active = models.BooleanField(default=False)
    monitor = models.IntegerField(verbose_name="ID монитора")
    screen_size = models.CharField(max_length=255, verbose_name="Размеры экрана")
    keyboard_layout = models.TextField(verbose_name="Раскладка клавиатуры")
    global_activation = models.ForeignKey(GlobalActive, on_delete=models.CASCADE, blank=True, null=True)
    telegram_id = models.BigIntegerField(verbose_name="telegram_id", blank=True, null=True)

    def __str__(self):
        return f'{self.name_cmdr} - {self.active}'
