from django.contrib import admin
from .models import Posts
# Register your models here.
admin.site.site_header = "Tindatríóið"

class PostsAdmin(admin.ModelAdmin):
    list_display = ('name','subject','from_email','message','lesid')
    list_filter = ['lesid']
    list_editable = ['lesid']

admin.site.register(Posts,PostsAdmin)
