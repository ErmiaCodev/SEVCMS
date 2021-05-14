from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status')
	list_filter = ('publish', 'status')
	search_fields = ('title', 'description')
	prepopulated_fields = {'slug': ('title',)}
	order = ['-status', 'publish']

admin.site.register(Post, PostAdmin)


admin.site.register(Avatar)


admin.site.register(Comment)
