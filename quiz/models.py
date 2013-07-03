from django.db import models
from django.conf import settings
from yamlfield import YAMLField


class Quiz(models.Model):
	"""
	Contains a set of questions, possible answers and feedbacks (in the structure field).  
	See README for proper construction of the quiz.
	"""
	name 		= models.CharField(max_length=255)
	description	= models.TextField(blank=True, null=True)
	structure   = YAMLField()

	class Meta:
		verbose_name_plural = "quizzes"

	def get_feedback(self, question_key, answer_key):
		"""
		Get the feedback that should be given if the user chooses a certain answer to a certain question.
		"""
		print "QN %s" % question_key	
		for question in self.structure['questions']:
			print question['key']
			if question['key'] == question_key:
				for answer in question['answers']:
					if answer["key"] == answer_key:
						return answer['feedback']
		return "fix me"

	def __unicode__(self):
		return self.name


class Attempt(models.Model):
    """
    All the users responses to a given quiz.
    """
    user 	= models.ForeignKey(settings.AUTH_USER_MODEL)
    quiz 	= models.ForeignKey(Quiz)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Answers from %s" % (self.user.name)


class Answer(models.Model):
    """
    Represents one answer from a user.
    """
    attempt    	= models.ForeignKey(Attempt, related_name='answers')
    question 	= models.CharField(max_length=255)
    answer      = models.CharField(max_length=255)
    is_correct	= models.BooleanField(default=False)

    def __unicode__(self):
        return "%s: %s" % (self.question, self.answer)
