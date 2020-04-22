from django.apps import AppConfig

from .model.Grader import Grader

class WebappConfig(AppConfig):

	# Grader Object Instantiation
	gd = Grader()
	grader = gd.grade

class GraderConfig(AppConfig):
    name = 'grader'
