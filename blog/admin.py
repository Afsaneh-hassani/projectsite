from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','counted_view','status','published_date','created_date')
    list_filter=('status',)
    #ordering=['-created_date']
    search_fields=['title','content']
    #summernote_fields =('content',)



admin.site.register(Post,PostAdmin)

# Register your models here.
