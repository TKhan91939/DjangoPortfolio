from django.contrib import admin
from .models import Developer, Project
from django.utils.html import format_html


# Register your models here.
@admin.register(Developer)
class DevAdmin(admin.ModelAdmin):
    list_display = ["image", "first_name", "last_name", "alias", "id"]


    def image(self, obj):
        return format_html('<img src="{}" width="150"/>', obj.img.url)






@admin.register(Project)
class ProjAdmin(admin.ModelAdmin):
    list_display = ["image", "name", "description", "date", "link", "gist", "git_id"]


    def image(self, obj):
        return format_html('<img src="{}" width="200"/>', obj.img.url)

    

