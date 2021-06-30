from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(
		max_length = 50,
	)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'


class Notice(models.Model):
	subject = models.CharField(
		max_length = 50,	
	)
	body = models.TextField(
		max_length = 200,
	)
	publishedDate = models.DateField(
		null = True,
		blank = True,
	)
	createdDate = models.DateField(
		auto_now_add = True,	
	)
	isPublished = models.BooleanField(
		default = False,
	)
	category = models.ForeignKey(
		'Category',
		on_delete = models.CASCADE
	)


	def __str__(self):
		return self.subject

		
class Message(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100,blank=True,null=True)
	email = models.EmailField(blank=True,null=True)
	sent_on = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
						