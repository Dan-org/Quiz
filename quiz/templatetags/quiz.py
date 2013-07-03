import os, re, urlparse
import ttag
from xml.etree import ElementTree

from django import template
from django.core.urlresolvers import reverse
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.template.defaulttags import URLNode, url
from django.template import Template, Context, loader, RequestContext, Variable, TemplateSyntaxError
from django.shortcuts import get_object_or_404, render_to_response

from django.utils.encoding import force_unicode

#from quiz.models import Quiz


register = template.Library()


@register.tag(name="quiz")
class QuizTag(ttag.Tag):
    """
    Tag will render a quiz in a template.
    :param quiz_name: the name of the quiz in the database 
    """
    name = ttag.BasicArg()        
    
    def render(self, context):
        data = self.resolve(context)
        name = _strip_quotes(data['name'])
        
        quiz = Quiz.objects.get(name=name)
        
        ## load the header template
        t = template.loader.get_template("quiz/quiz.html")
        c = Context({'quiz':quiz})
        return t.render(c)


def _strip_quotes(arg):
    if not (arg[0] == arg[-1] and arg[0] in ('"', "'")):
        raise template.TemplateSyntaxError("Argument %s should be in quotes" % arg)
    return arg[1:-1]
