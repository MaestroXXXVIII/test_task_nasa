from django.db import models
from filer.fields.image import FilerImageField

class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = FilerImageField(on_delete=models.CASCADE, related_name='slider_image')
    my_order = models.PositiveIntegerField(default=0, null=False, blank=False, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"