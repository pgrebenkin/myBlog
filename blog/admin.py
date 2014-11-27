from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from blog import models

# Register your models here.
class PostAdmin(MarkdownModelAdmin):
	list_display = ("title", "created", "modified","publish", "numofseen")
	prepopulated_fields = {"slug":("title",)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Label)