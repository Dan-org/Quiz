import ttag
from django import template
from django.template import Template, Context

from ..models import Quiz
from ..forms import CreateQuizForm


register = template.Library()


@register.tag(name="quiz")
class QuizTag(ttag.Tag):
    """
    Tag will render a quiz in a template.
    :param quiz_name: the name of the quiz in the database 
    """
    name = ttag.BasicArg()        
    
    def render(self, context):        
        try:
            data = self.resolve(context)
            name = _strip_quotes(data['name'])
            
            request = context['request']

            quiz = Quiz.objects.get(name=name)
            
            form = CreateQuizForm(request, quiz=quiz, user=request.user)

            ## load the header template
            t = template.loader.get_template("quiz/quiz.html")
            c = Context({'quiz':quiz, 'form':form})
            return t.render(c)
        except:
            return ""



def _strip_quotes(arg):
    if not (arg[0] == arg[-1] and arg[0] in ('"', "'")):
        raise template.TemplateSyntaxError("Argument %s should be in quotes" % arg)
    return arg[1:-1]
