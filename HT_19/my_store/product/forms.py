from django.forms import ModelForm, Textarea
from .models import ScrapingTask


class IDForm(ModelForm):
   class Meta:
      model = ScrapingTask
      fields = ('ids',)
      widgets = {'ids': Textarea(attrs={'cols': 20, 'rows': 10})}
