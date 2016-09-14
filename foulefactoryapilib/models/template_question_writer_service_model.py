# -*- coding: utf-8 -*-

"""
    foulefactoryapilib.models.template_question_writer_service_model
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 09/14/2016
"""
from .base_model import BaseModel

class TemplateQuestionWriterServiceModel(BaseModel):

    """Implementation of the 'TemplateQuestionWriterServiceModel' model.

    TODO: type model description here.

    Attributes:
        title (string): TODO: type description here.
        require (bool): TODO: type description here.
        id_template_object_question_type (int): TODO: type description here.
        order (int): TODO: type description here.
        option (string): TODO: type description here.
        choices (list of string): TODO: type description here.

    """

    def __init__(self, 
                 title = None,
                 require = None,
                 id_template_object_question_type = None,
                 order = None,
                 option = None,
                 choices = None):
        """Constructor for the TemplateQuestionWriterServiceModel class"""
        
        # Initialize members of the class
        self.title = title
        self.require = require
        self.id_template_object_question_type = id_template_object_question_type
        self.order = order
        self.option = option
        self.choices = choices

        # Create a mapping from Model property names to API property names
        self.names = {
            "title" : "Title",
            "require" : "Require",
            "id_template_object_question_type" : "IdTemplateObjectQuestionType",
            "order" : "Order",
            "option" : "Option",
            "choices" : "Choices",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            title = dictionary.get("Title")
            require = dictionary.get("Require")
            id_template_object_question_type = dictionary.get("IdTemplateObjectQuestionType")
            order = dictionary.get("Order")
            option = dictionary.get("Option")
            choices = dictionary.get("Choices")
            # Return an object of this model
            return cls(title,
                       require,
                       id_template_object_question_type,
                       order,
                       option,
                       choices)
