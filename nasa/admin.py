from django.contrib import admin
from .models import Slider
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Slider
    list_display = ['title', 'get_image', 'order']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100"')

    get_image.short_description = "Изображение"
