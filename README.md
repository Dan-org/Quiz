To use quizzes in the Loft
-------------------

- add the git repository to requirements
- run pip
- add 'quiz' to intalled apps
- include quiz urls for ajax calls to work url(r'', include('quiz.urls')),
- add_to_builtins('quiz.templatetags.quiz')  # for discourse tags to work

in the templates:
- {% load quiz %}
- <script type="text/javascript" src="{{STATIC_URL}}js/quiz.js"></script>
- {% quiz 'My Quiz Name' %}


To Instal the demo
-------------------
Prerequisites for Mac OS:
Make sure you have the XCode development environment and the Development Command Line Tools.  They can be downloaded from https://developer.apple.com/downloads/index.action, you need Xcode 4.6 or higher, and "Command Line Tools" for your version of your OS.

Prerequisites for Linux:
Make sure you have python 2.6 or higher installed (it should be).  You can check by running "python" and looking at the first line.  Also make sure you have python-setuptools by seeing if the command "easy_install" is available.  If that command fails to run, try going to http://pypi.python.org/pypi/setuptools

Step 1:
Make sure you have pip and virtualenv installed by doing:

  > sudo easy_install pip virtualenv
  ...
  Finished processing dependencies for virtualenv

Step 2:
In the project root, create a python virtual environment named "env".

  > virtualenv env
  New python executable in env/bin/python
  Installing setuptools............done.
  Installing pip...............done.


Step 3:
Install the project requirements.  Make sure you see "Successfully installed ..." at the end.  Otherwise check troubleshooting, below.

  > env/bin/pip install -r requirements.txt
  ...
  Successfully installed Django
  Cleaning up...

Step 4:

  > ./manage.py syncdb
  Ceating tables ...
  ...
  Would you like to create one now? (yes/no):

It will ask you to create a user, go ahead and create one for yourself.  That user will only be local to *your* machine so don't expect it to be anywhere else.  If this fails, or you want to create a user later see "Creating An Admin User Via The Command Line", below.  Also, there is by default a user with email "admin@designforamerica.com" and password "pass".

Step 5:
  
  > ./manage.py runserver
  ...
  Development server is running at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.

This will start up the server, running.  Visit http://127.0.0.1:8000/ in your browser now.
Changes you make should automatically up





The site has nice description of how to do ajax forms
  http://www.jonhill.ca/programming/ajax-forms-in-django


Here is an example quiz with two questions:
  1. Did you like DOLE?
    A1. Yes  => Good job
    A2. No   => What??!!
  2. Did you really like DOLE?
    A1. Yes I really did  => Good job
    A2. No  I really did not  => What??!!


questions:
- answers:
  - feedback: Good job
    is_correct: true
    key: 'yes'
    label: Yes I did
  - feedback: What??!!
    is_correct: false
    key: 'no'
    label: No I did not
  key: like-dole
  label: Did you like dole?
- answers:
  - feedback: Good job
    is_correct: true
    key: 'yes'
    label: Yes I really did
  - feedback: What??!!
    is_correct: false
    key: 'no'
    label: No I really did not
  key: really-like-dole
  label: Did you really like dole?
title: The dole quiz


Run tests
------
./manage.py test quiz

Save fixtures
------
./manage.py dumpdata quiz.Quiz quiz.Attempt quiz.Answer > quiz/fixtures/quiz_testing.json

Load fixtures
------
./manage.py loaddata quiz_testing
