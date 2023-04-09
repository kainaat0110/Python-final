from django.forms import ModelForm
from .models import Diary_entry

class EntryForm(ModelForm):
    class Meta:
        model = Diary_entry
        fields =('text', )
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'textarea','placeholder':' Share your thoughts..'})
