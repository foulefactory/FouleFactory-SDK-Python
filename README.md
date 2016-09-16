# Getting Started
## How to Build


You must have Python greater than 2.7 installed in your system to build and run your SDK files. 
The generated code has dependencies over external libraries like nose, jsonpickle, etc. These dependencies are defined in the ```requirements.txt``` file that comes with the SDK. 
To resolve these dependencies, we use the PIP Dependency manager. Install it by following steps at https://pip.pypa.io/en/stable/installing/

The paths of Python and PIP must be properly set in the environment variables. Open command prompt and type ```pip --version```. 
This should display the current version of the PIP Dependency Manager installed if the installation was successful.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK. 
Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](http://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=FouleFactory Api-Python)


## How to Use

The following section explains how to use the FouleFactoryApi library in a new project.

#### 1. Open Project in an IDE
Open an IDE for Python like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=openProject0&workspaceFolder=FouleFactory Api-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=openProject1&workspaceFolder=FouleFactory Api-Python&projectName=foulefactoryapilib)     


#### 2. Add a new Test Project
Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=FouleFactory Api-Python&projectName=foulefactoryapilib)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=createFile&workspaceFolder=FouleFactory Api-Python&projectName=foulefactoryapilib)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines
   ```Python
   from foulefactoryapilib.foulefactoryapi_client import *
   ```
![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=FouleFactory Api-Python&libraryName=foulefactoryapilib.foulefactoryapi_client&projectName=foulefactoryapilib)

After this you can add code to initialize the client library and acquire the instance of a Controller class. Sample code to initialize the client library and using controller methods is given in the subsequent sections.


#### 3. Run the Test Project
To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](http://apidocs.io/illustration/python?step=runProject&workspaceFolder=FouleFactory Api-Python&libraryName=foulefactoryapilib.foulefactoryapi_client&projectName=foulefactoryapilib)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'nosetests'

## Initialization

#### Authentication and Initialization
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = "basic_auth_user_name" # The username to use with basic authentication
basic_auth_password = "basic_auth_password" # The password to use with basic authentication

client = FouleFactoryApiClient(basic_auth_user_name, basic_auth_password)
```

# Class Reference
## <a name="list_of_controllers"></a>List of Controllers

* [TaskAnswerTextsController](#task_answer_texts_controller)
* [TaskAnswerChoicesController](#task_answer_choices_controller)
* [ProjectsController](#projects_controller)
* [CsvFilesController](#csv_files_controller)
* [AccountController](#account_controller)
* [TemplatesController](#templates_controller)
* [TasksController](#tasks_controller)
* [TaskLinesController](#task_lines_controller)

## <a name="task_answer_texts_controller"></a>![Class: ](http://apidocs.io/img/class.png ".TaskAnswerTextsController") TaskAnswerTextsController


#### Get controller instance
An instance of the ``` TaskAnswerTextsController ``` class can be accessed from the API Client.
```python
 task_answer_texts_client = client.task_answer_texts
```

### <a name="get_task_answer_texts_get"></a>![Method: ](http://apidocs.io/img/method.png ".TaskAnswerTextsController.get_task_answer_texts_get") get_task_answer_texts_get

> Get task answer text by id

```python
def get_task_answer_texts_get(self,
                                  id,
                                  accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = task_answer_texts_client.get_task_answer_texts_get(id, accept_language)

```





[Back to List of Controllers](#list_of_controllers)
## <a name="task_answer_choices_controller"></a>![Class: ](http://apidocs.io/img/class.png ".TaskAnswerChoicesController") TaskAnswerChoicesController


#### Get controller instance
An instance of the ``` TaskAnswerChoicesController ``` class can be accessed from the API Client.
```python
 task_answer_choices_client = client.task_answer_choices
```

### <a name="get_task_answer_choices_get"></a>![Method: ](http://apidocs.io/img/method.png ".TaskAnswerChoicesController.get_task_answer_choices_get") get_task_answer_choices_get

> Get task answer choice by id

```python
def get_task_answer_choices_get(self,
                                    id,
                                    accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = task_answer_choices_client.get_task_answer_choices_get(id, accept_language)

```





[Back to List of Controllers](#list_of_controllers)
## <a name="projects_controller"></a>![Class: ](http://apidocs.io/img/class.png ".ProjectsController") ProjectsController


#### Get controller instance
An instance of the ``` ProjectsController ``` class can be accessed from the API Client.
```python
 projects_client = client.projects
```

### <a name="create_projects_create_project"></a>![Method: ](http://apidocs.io/img/method.png ".ProjectsController.create_projects_create_project") create_projects_create_project

> Create new project

```python
def create_projects_create_project(self,
                                       project,
                                       accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| project |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
project = ProjectWriterServiceModel()
accept_language = 'fr'

result = projects_client.create_projects_create_project(project, accept_language)

```





### <a name="get_projects_get_user_projects"></a>![Method: ](http://apidocs.io/img/method.png ".ProjectsController.get_projects_get_user_projects") get_projects_get_user_projects

> Get All projects

```python
def get_projects_get_user_projects(self)
```

#### Example Usage:
```python

result = projects_client.get_projects_get_user_projects()

```





### <a name="get_projects_get_project_files"></a>![Method: ](http://apidocs.io/img/method.png ".ProjectsController.get_projects_get_project_files") get_projects_get_project_files

> Get csv files by project id

```python
def get_projects_get_project_files(self,
                                       id,
                                       accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = projects_client.get_projects_get_project_files(id, accept_language)

```





### <a name="get_projects_get_project_task_lines"></a>![Method: ](http://apidocs.io/img/method.png ".ProjectsController.get_projects_get_project_task_lines") get_projects_get_project_task_lines

> Get task lines by project id

```python
def get_projects_get_project_task_lines(self,
                                            id,
                                            accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = projects_client.get_projects_get_project_task_lines(id, accept_language)

```





### <a name="get_projects_get_project_tasks"></a>![Method: ](http://apidocs.io/img/method.png ".ProjectsController.get_projects_get_project_tasks") get_projects_get_project_tasks

> Get tasks by project id

```python
def get_projects_get_project_tasks(self,
                                       id,
                                       accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = projects_client.get_projects_get_project_tasks(id, accept_language)

```





### <a name="get_projects_get"></a>![Method: ](http://apidocs.io/img/method.png ".ProjectsController.get_projects_get") get_projects_get

> Get project by id

```python
def get_projects_get(self,
                         id,
                         accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = projects_client.get_projects_get(id, accept_language)

```





[Back to List of Controllers](#list_of_controllers)
## <a name="csv_files_controller"></a>![Class: ](http://apidocs.io/img/class.png ".CsvFilesController") CsvFilesController


#### Get controller instance
An instance of the ``` CsvFilesController ``` class can be accessed from the API Client.
```python
 csv_files_client = client.csv_files
```

### <a name="create_csv_files_create_csv_file"></a>![Method: ](http://apidocs.io/img/method.png ".CsvFilesController.create_csv_files_create_csv_file") create_csv_files_create_csv_file

> Create new csv file

```python
def create_csv_files_create_csv_file(self,
                                         csvfiles,
                                         accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| csvfiles |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
csvfiles = CsvFileWriterServiceModel()
accept_language = 'fr'

result = csv_files_client.create_csv_files_create_csv_file(csvfiles, accept_language)

```





### <a name="get_csv_files_get"></a>![Method: ](http://apidocs.io/img/method.png ".CsvFilesController.get_csv_files_get") get_csv_files_get

> Get csv file by id

```python
def get_csv_files_get(self,
                          id,
                          accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = csv_files_client.get_csv_files_get(id, accept_language)

```





[Back to List of Controllers](#list_of_controllers)
## <a name="account_controller"></a>![Class: ](http://apidocs.io/img/class.png ".AccountController") AccountController


#### Get controller instance
An instance of the ``` AccountController ``` class can be accessed from the API Client.
```python
 account_client = client.account
```

### <a name="get_account_validate_transaction"></a>![Method: ](http://apidocs.io/img/method.png ".AccountController.get_account_validate_transaction") get_account_validate_transaction

> TODO: Add a method description

```python
def get_account_validate_transaction(self,
                                         transaction_id,
                                         accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| transactionId |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
transaction_id = 'transactionId'
accept_language = 'fr'

result = account_client.get_account_validate_transaction(transaction_id, accept_language)

```





### <a name="create_account_pay_in"></a>![Method: ](http://apidocs.io/img/method.png ".AccountController.create_account_pay_in") create_account_pay_in

> Payin

```python
def create_account_pay_in(self,
                              payin,
                              accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| payin |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
payin = PayinServiceModel()
accept_language = 'fr'

result = account_client.create_account_pay_in(payin, accept_language)

```





### <a name="get_account_get_wallet"></a>![Method: ](http://apidocs.io/img/method.png ".AccountController.get_account_get_wallet") get_account_get_wallet

> Get wallet

```python
def get_account_get_wallet(self)
```

#### Example Usage:
```python

result = account_client.get_account_get_wallet()

```





### <a name="create_account_create_account"></a>![Method: ](http://apidocs.io/img/method.png ".AccountController.create_account_create_account") create_account_create_account

> *Tags:*  ``` Skips Authentication ``` 

> Create new account

```python
def create_account_create_account(self,
                                      account,
                                      accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| account |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
account = AccountWriterServiceModel()
accept_language = 'fr'

result = account_client.create_account_create_account(account, accept_language)

```





### <a name="get_account_get"></a>![Method: ](http://apidocs.io/img/method.png ".AccountController.get_account_get") get_account_get

> Get my account

```python
def get_account_get(self)
```

#### Example Usage:
```python

result = account_client.get_account_get()

```





[Back to List of Controllers](#list_of_controllers)
## <a name="templates_controller"></a>![Class: ](http://apidocs.io/img/class.png ".TemplatesController") TemplatesController


#### Get controller instance
An instance of the ``` TemplatesController ``` class can be accessed from the API Client.
```python
 templates_client = client.templates
```

### <a name="create_templates_create_template"></a>![Method: ](http://apidocs.io/img/method.png ".TemplatesController.create_templates_create_template") create_templates_create_template

> Create new template

```python
def create_templates_create_template(self,
                                         template,
                                         accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| template |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
template = TemplateNewWriterServiceModel()
accept_language = 'fr'

result = templates_client.create_templates_create_template(template, accept_language)

```





### <a name="get_templates_get_templates"></a>![Method: ](http://apidocs.io/img/method.png ".TemplatesController.get_templates_get_templates") get_templates_get_templates

> Get all user templates id

```python
def get_templates_get_templates(self)
```

#### Example Usage:
```python

result = templates_client.get_templates_get_templates()

```





### <a name="get_templates_get_template"></a>![Method: ](http://apidocs.io/img/method.png ".TemplatesController.get_templates_get_template") get_templates_get_template

> Get template by id

```python
def get_templates_get_template(self,
                                   id_template,
                                   accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| idTemplate |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id_template = 187
accept_language = 'fr'

result = templates_client.get_templates_get_template(id_template, accept_language)

```





[Back to List of Controllers](#list_of_controllers)
## <a name="tasks_controller"></a>![Class: ](http://apidocs.io/img/class.png ".TasksController") TasksController


#### Get controller instance
An instance of the ``` TasksController ``` class can be accessed from the API Client.
```python
 tasks_client = client.tasks
```

### <a name="update_tasks_validate"></a>![Method: ](http://apidocs.io/img/method.png ".TasksController.update_tasks_validate") update_tasks_validate

> Validate task

```python
def update_tasks_validate(self,
                              task,
                              accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| task |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
task = TaskValidationWriterServiceModel()
accept_language = 'fr'

result = tasks_client.update_tasks_validate(task, accept_language)

```





### <a name="get_tasks_get_answer_choices"></a>![Method: ](http://apidocs.io/img/method.png ".TasksController.get_tasks_get_answer_choices") get_tasks_get_answer_choices

> Get task answer choices by task id

```python
def get_tasks_get_answer_choices(self,
                                     id,
                                     accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = tasks_client.get_tasks_get_answer_choices(id, accept_language)

```





### <a name="get_tasks_get_answer_texts"></a>![Method: ](http://apidocs.io/img/method.png ".TasksController.get_tasks_get_answer_texts") get_tasks_get_answer_texts

> Get task answer texts by task id

```python
def get_tasks_get_answer_texts(self,
                                   id,
                                   accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = tasks_client.get_tasks_get_answer_texts(id, accept_language)

```





### <a name="get_tasks_get"></a>![Method: ](http://apidocs.io/img/method.png ".TasksController.get_tasks_get") get_tasks_get

> Get task by id

```python
def get_tasks_get(self,
                      id,
                      accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = tasks_client.get_tasks_get(id, accept_language)

```





[Back to List of Controllers](#list_of_controllers)
## <a name="task_lines_controller"></a>![Class: ](http://apidocs.io/img/class.png ".TaskLinesController") TaskLinesController


#### Get controller instance
An instance of the ``` TaskLinesController ``` class can be accessed from the API Client.
```python
 task_lines_client = client.task_lines
```

### <a name="create_task_lines_create_task_line"></a>![Method: ](http://apidocs.io/img/method.png ".TaskLinesController.create_task_lines_create_task_line") create_task_lines_create_task_line

> Create new task line

```python
def create_task_lines_create_task_line(self,
                                           task_line,
                                           accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| taskLine |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
task_line = TaskLinesWriterServiceModel()
accept_language = 'fr'

result = task_lines_client.create_task_lines_create_task_line(task_line, accept_language)

```





### <a name="get_task_lines_get_tasks_by_line"></a>![Method: ](http://apidocs.io/img/method.png ".TaskLinesController.get_task_lines_get_tasks_by_line") get_task_lines_get_tasks_by_line

> Get tasks by task line id

```python
def get_task_lines_get_tasks_by_line(self,
                                         id,
                                         accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = task_lines_client.get_task_lines_get_tasks_by_line(id, accept_language)

```





### <a name="get_task_lines_get"></a>![Method: ](http://apidocs.io/img/method.png ".TaskLinesController.get_task_lines_get") get_task_lines_get

> Get task line by id

```python
def get_task_lines_get(self,
                           id,
                           accept_language = 'fr')
```

#### Parameters: 

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| acceptLanguage |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage:
```python
id = 187
accept_language = 'fr'

result = task_lines_client.get_task_lines_get(id, accept_language)

```





[Back to List of Controllers](#list_of_controllers)


