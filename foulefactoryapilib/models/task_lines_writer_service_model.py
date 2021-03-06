# -*- coding: utf-8 -*-

"""
    foulefactoryapilib.models.task_lines_writer_service_model
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 09/16/2016
"""
from .base_model import BaseModel

class TaskLinesWriterServiceModel(BaseModel):

    """Implementation of the 'TaskLinesWriterServiceModel' model.

    TODO: type model description here.

    Attributes:
        id_project (int): TODO: type description here.
        task_columns (list of string): TODO: type description here.

    """

    def __init__(self, 
                 id_project = None,
                 task_columns = None):
        """Constructor for the TaskLinesWriterServiceModel class"""
        
        # Initialize members of the class
        self.id_project = id_project
        self.task_columns = task_columns

        # Create a mapping from Model property names to API property names
        self.names = {
            "id_project" : "IdProject",
            "task_columns" : "TaskColumns",
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
            id_project = dictionary.get("IdProject")
            task_columns = dictionary.get("TaskColumns")
            # Return an object of this model
            return cls(id_project,
                       task_columns)
