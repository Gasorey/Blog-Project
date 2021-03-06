from django import forms

from .models import Comment,Project


class ProjectForm(forms.ModelForm):
    
    class Meta():
        model = Project
        fields = ('author','project_name','description')

        widgets = {
            'project_name':forms.TextInput(attrs={'class':'textinputclass'}),
            'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea '}),
            
        }

class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }