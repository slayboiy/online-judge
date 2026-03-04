from .models import Task, TaskTest, Submission, Language
from django.forms import ModelForm, TextInput, Textarea, NumberInput
from django.forms import inlineformset_factory
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'time_limit']
        
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
            }),
            'time_limit': NumberInput(attrs={
                'class': 'form-control',
            }),    
        }
        labels = {
            'title': 'Название задачи',
            'description': 'Описание задачи',
            'time_limit': 'Ограничение по времени (в секундах)'
            
        }



class TestForm(ModelForm):
    class Meta:
        model = TaskTest
        fields = ['input_data', 'expected_output']
        
        widgets = {
            'input_data': Textarea(attrs={
                'class': 'form-control',
            }),
            'expected_output': Textarea(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'input_data': "Входные данные",
            'expected_output': 'Выходные данные'
        }
        
        
forms_tests = inlineformset_factory(
    Task, 
    TaskTest,
    form=TestForm, 
    extra=0, 
    can_delete=True
)

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['language', 'source_code']
        
        widgets = {
            'source_code': Textarea(attrs={
                'class': 'form-control',
                'id': 'code',
            })
        }
        
        labels = {
            'language': 'Язык Программирования',
            'source_code': ''
        }

# class LanguageForm(ModelForm):
#     language_select = forms.ModelChoiceField(
#         queryset=Language.objects.all(),
#         initial=1,
#         label='Язык программирования: '
#     )
#     class Meta:
#         model = Language
#         fields = []

             
        
            
        
        