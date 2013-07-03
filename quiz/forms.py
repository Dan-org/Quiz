from django.forms import Form, ModelForm, ModelChoiceField, ChoiceField, CharField, BooleanField
from django.forms.widgets import HiddenInput, RadioSelect, Textarea
from django.contrib import messages
from django.utils.text import slugify
from models import Quiz, Attempt, Answer


class EasyForm(object):
    """
    An easier way of doing forms so that they take requests instead of blank data.  Also handles
    creating the message, and can be extended later to do other things like trigger signals.
    """
    methods = ['post', 'put']

    def __init__(self, request, data = None, instance=None, msg="Form submitted.", methods=None):
        self.methods = methods or self.__class__.methods
        self.request = request
        self.msg = msg
        self.initial = dict(tup for tup in request.GET.items())
        
        kwargs = {'initial': self.initial}
        if instance is not None:
            kwargs.update({'instance': instance})

        if request.method.lower() in self.methods:
            super(EasyForm, self).__init__(data or request.POST, request.FILES, **kwargs)
        else:
            super(EasyForm, self).__init__(**kwargs)

    def is_valid(self):
        if self.request.method.lower() not in self.methods:
            return False
        return super(EasyForm, self).is_valid()

    def save(self):
        instance = super(EasyForm, self).save()
        if not self.request.is_ajax():
            messages.add_message(self.request, messages.INFO, self.msg)
        return instance




class CreateQuizForm(EasyForm, Form):
    """
    Creates a form for a quiz with an arbitrary number of questions.
    """
    def __init__(self, *args, **kwargs):
        self.quiz = kwargs.pop('quiz')
        self.user = kwargs.pop('user')

        super(CreateQuizForm, self).__init__(*args, **kwargs)
        self.build()

    def build(self):
        self._questions = []
        # what about title??
        for index, question in enumerate(self.quiz.structure['questions']):
            self.build_radio(question, index) 

    def build_radio(self, question, index):
        #key = '%s-%s' % (group['slug'], criterion['slug'])        
        key = question['key']
        choices = [(answer['key'], answer['label'],) for i, answer in enumerate(question['answers'])]
        feedbacks = [answer['feedback'] for answer in question['answers']]

        # figure out previous responses if any
        initial = '' 
        if self.user.is_authenticated():
            try:
                attempt = Attempt.objects.get(quiz=self.quiz)
                answer  = Answer.objects.get(attempt=attempt, question=key)
                initial = answer.answer
            except:
                pass

        field = ChoiceField(label=question['label'], widget=RadioSelect, choices=choices, initial=initial)
        self.fields['%s-field' % key] = field        
        self._questions.append({
            'key': key,                        
            'label': question['label'],
            'type': 'radio',           
            'feedbacks': feedbacks,
        })

    def save(self, quiz):
        attempt, _ = Attempt.objects.get_or_create(user=self.request.user, defaults={'quiz': self.quiz})
        attempt.answers.all().delete()
        for question in self._questions:
            key = question['key']
            attempt.question.create(
                key     = key,
                value   = self.cleaned_data['%s-field' % key],                
            )
        return attempt

    def questions(self):
        for question in self._questions:
            question['field'] = self['%s-field' % question['key']]            
            yield question


#class AjaxForm( Form ):
#    input = CharField( required=True )
 
# class AjaxForm(EasyForm, Form ):

#     def __init__(self, *args, **kwargs):        
#         super(AjaxForm, self).__init__(*args, **kwargs)        
#         self.fields['input'] = CharField( required=True )
    
#     def save(self):
#         return None;
    

