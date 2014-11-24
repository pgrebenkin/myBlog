from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from blog import models

# Register your models here.
class EntryAdmin(MarkdownModelAdmin):
	list_display = ("title", "created")
	prepopulated_fields = {"slug":("title",)}

admin.site.register(models.Entry, EntryAdmin)