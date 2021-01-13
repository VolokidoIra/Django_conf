from django.db import models


class Save_File(models.Model):
    save_file = models.FileField('Выберете файл', upload_to='')

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

