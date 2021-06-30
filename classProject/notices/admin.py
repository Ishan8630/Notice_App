from django.contrib import admin
from .models import Category,Notice,Message

from django.db import models
from django.forms import Textarea

# Register your models here.
admin.site.register(Category)
#admin.site.register(Notice)

#to display the notices inside category
#class NoticeInline(admin.TabularInline):
#	model = Notice
#	extra = 1 
#	formfield_overrides = {
#		models.TextField : {'widget':Textarea(attrs={'rows':4,'cols':40})},
#	}
#class CategoryAdmin(admin.ModelAdmin):
#	model = Category
#	inlines = [ NoticeInline ]
#admin.site.register(Category,CategoryAdmin)


#to display notice in list to admin
class NoticeAdmin(admin.ModelAdmin):
	search_fields = ('subject','body',)
	list_filter = ('isPublished','createdDate','publishedDate')
	list_display = ('category','subject','body','createdDate','isPublished','publishedDate','new')

	def new(self,obj):
		
		return 'Test'

admin.site.register(Notice,NoticeAdmin)		

admin.site.register(Message)

admin.site.site_header = "KEC_Notices"
admin.site.site_title = "Notice Board"
admin.site.index_title