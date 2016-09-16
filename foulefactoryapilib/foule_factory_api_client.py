# -*- coding: utf-8 -*-

"""
    foulefactoryapilib.foule_factory_api_client

    This file was automatically generated by APIMATIC BETA v2.0 on 09/16/2016
"""

from .http import *
from .models import *
from .exceptions import *
from .decorators import *
from .controllers import *

class FouleFactoryApiClient(object):

    @lazy_property
    def task_answer_texts(self):
        return TaskAnswerTextsController()

    @lazy_property
    def task_answer_choices(self):
        return TaskAnswerChoicesController()

    @lazy_property
    def projects(self):
        return ProjectsController()

    @lazy_property
    def csv_files(self):
        return CsvFilesController()

    @lazy_property
    def account(self):
        return AccountController()

    @lazy_property
    def templates(self):
        return TemplatesController()

    @lazy_property
    def tasks(self):
        return TasksController()

    @lazy_property
    def task_lines(self):
        return TaskLinesController()



