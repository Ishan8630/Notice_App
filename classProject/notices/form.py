from django import forms
from .models import Message

class MsgForm(forms.ModelForm):
	class Meta:
		model = Message
		#fields = "__all__"
		fields = ['name','phone','message']
		labels={
			'name' : ('Full Name'),
			'phone' : ('Phone Number'),
		}
		help_texts = {
			'name' : ('Enter your full name'),
		}