from django.forms import ModelForm
from .models import School, Review

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'})
        # self.fields['establishment_name'].widget.attrs.update({'class': 'flex flex-col form-control input rounded'})
        # self.fields['town'].widget.attrs.update({'class': 'form-control'})
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']
        labels = {
            'body': 'Add a comment with your vote',
            'value': 'Place your Vote'
        }
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'})
        # self.fields['establishment_name'].widget.attrs.update({'class': 'flex flex-col form-control input rounded'})
        # self.fields['town'].widget.attrs.update({'class': 'form-control