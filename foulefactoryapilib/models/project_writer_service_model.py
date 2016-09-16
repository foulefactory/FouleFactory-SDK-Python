# -*- coding: utf-8 -*-

"""
    foulefactoryapilib.models.project_writer_service_model
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 09/16/2016
"""
import dateutil.parser
from .base_model import BaseModel

class ProjectWriterServiceModel(BaseModel):

    """Implementation of the 'ProjectWriterServiceModel' model.

    TODO: type model description here.

    Attributes:
        id_template (int): TODO: type description here.
        title (string): TODO: type description here.
        estimated_time_per_task (string): TODO: type description here.
        nb_supplier_per_task (int): TODO: type description here.
        amount_without_tax_per_task (int): TODO: type description here.
        automatic_validation (bool): TODO: type description here.
        max_end_date (DateTime): TODO: type description here.
        id_certification (int): TODO: type description here.
        url_notification (string): TODO: type description here.

    """

    def __init__(self, 
                 id_template = None,
                 title = None,
                 estimated_time_per_task = None,
                 nb_supplier_per_task = None,
                 amount_without_tax_per_task = None,
                 automatic_validation = None,
                 max_end_date = None,
                 id_certification = None,
                 url_notification = None):
        """Constructor for the ProjectWriterServiceModel class"""
        
        # Initialize members of the class
        self.id_template = id_template
        self.title = title
        self.estimated_time_per_task = estimated_time_per_task
        self.nb_supplier_per_task = nb_supplier_per_task
        self.amount_without_tax_per_task = amount_without_tax_per_task
        self.automatic_validation = automatic_validation
        self.max_end_date = max_end_date
        self.id_certification = id_certification
        self.url_notification = url_notification

        # Create a mapping from Model property names to API property names
        self.names = {
            "id_template" : "IdTemplate",
            "title" : "Title",
            "estimated_time_per_task" : "EstimatedTimePerTask",
            "nb_supplier_per_task" : "NbSupplierPerTask",
            "amount_without_tax_per_task" : "AmountWithoutTaxPerTask",
            "automatic_validation" : "AutomaticValidation",
            "max_end_date" : "MaxEndDate",
            "id_certification" : "IdCertification",
            "url_notification" : "UrlNotification",
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
            id_template = dictionary.get("IdTemplate")
            title = dictionary.get("Title")
            estimated_time_per_task = dictionary.get("EstimatedTimePerTask")
            nb_supplier_per_task = dictionary.get("NbSupplierPerTask")
            amount_without_tax_per_task = dictionary.get("AmountWithoutTaxPerTask")
            automatic_validation = dictionary.get("AutomaticValidation")
            max_end_date = dateutil.parser.parse(dictionary.get("MaxEndDate")) if dictionary.get("MaxEndDate") else None
            id_certification = dictionary.get("IdCertification")
            url_notification = dictionary.get("UrlNotification")
            # Return an object of this model
            return cls(id_template,
                       title,
                       estimated_time_per_task,
                       nb_supplier_per_task,
                       amount_without_tax_per_task,
                       automatic_validation,
                       max_end_date,
                       id_certification,
                       url_notification)
