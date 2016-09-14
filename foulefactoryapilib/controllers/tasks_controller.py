# -*- coding: utf-8 -*-

"""
    foulefactoryapilib.controllers.tasks_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 09/14/2016
"""

from .base_controller import *



class TasksController(BaseController):

    """A Controller to access Endpoints in the foulefactoryapilib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def update_tasks_validate(self,
                              task,
                              accept_language = 'fr'):
        """Does a PUT request to /v1.1/tasks.

        Validate task

        Args:
            task (TaskValidationWriterServiceModel): TODO: type description
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
        _query_builder += '/v1.1/tasks'
        
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(task), username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

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



    def get_tasks_get_answer_choices(self,
                                     id,
                                     accept_language = 'fr'):
        """Does a GET request to /v1.1/tasks/{id}/taskAnswerChoices.

        Get task answer choices by task id

        Args:
            id (int): TODO: type description here. Example: 
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
        _query_builder += '/v1.1/tasks/{id}/taskAnswerChoices'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
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



    def get_tasks_get_answer_texts(self,
                                   id,
                                   accept_language = 'fr'):
        """Does a GET request to /v1.1/tasks/{id}/taskAnswerTexts.

        Get task answer texts by task id

        Args:
            id (int): TODO: type description here. Example: 
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
        _query_builder += '/v1.1/tasks/{id}/taskAnswerTexts'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
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



    def get_tasks_get(self,
                      id,
                      accept_language = 'fr'):
        """Does a GET request to /v1.1/tasks/{id}.

        Get task by id

        Args:
            id (int): TODO: type description here. Example: 
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
        _query_builder += '/v1.1/tasks/{id}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'id': id
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


