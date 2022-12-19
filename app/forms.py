from dataclasses import Field, fields
from django.forms import FileField, ModelForm 

from app.models import TODO 
class TODOForm(ModelForm): 
    class Meta: 
        model=TODO 
        fields=['title', 'status', 'priority']
        
