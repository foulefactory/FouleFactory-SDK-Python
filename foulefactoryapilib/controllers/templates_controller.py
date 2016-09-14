# -*- coding: utf-8 -*-

"""
    foulefactoryapilib.controllers.templates_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 09/14/2016
"""

from .base_controller import *



class TemplatesController(BaseController):

    """A Controller to access Endpoints in the foulefactoryapilib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def create_templates_create_template(self,
                                         template,
                                         accept_language = 'fr'):
        """Does a POST request to /v1.1/templates.

        Create new template

        Args:
            template (TemplateNewWriterServiceModel): TODO: type description
                here. Example: 
            accept_language (string, optional): TODO: type description here.
                Example: fr

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/v1.1/templates'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'Accept-Language': accept_language
        }

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(template), username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body)



    def get_templates_get_templates(self):
        """Does a GET request to /v1.1/templates.

        Get all user templates id

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/v1.1/templates'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body)



    def get_templates_get_template(self,
                                   id_template,
                                   accept_language = 'fr'):
        """Does a GET request to /v1.1/templates/{idTemplate}.

        Get template by id

        Args:
            id_template (int): TODO: type description here. Example: 
            accept_language (string, optional): TODO: type description here.
                Example: fr

        Returns:
            mixed: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/v1.1/templates/{idTemplate}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'idTemplate': id_template
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'accept': 'application/json',
            'Accept-Language': accept_language
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body)


