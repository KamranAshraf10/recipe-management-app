Recipe Management App
=====================

Overview
--------

This Django-based application allows users to manage recipes, including adding new recipes, updating existing ones, and deleting them. It features a simple yet effective user interface for easy interaction.

Features
--------

*   **Add Recipes:** Users can add new recipes with a name, description, and image.
    
*   **Update Recipes:** Existing recipes can be updated.
    
*   **Delete Recipes:** Unwanted recipes can be removed from the system.
    

Tech Stack
----------

*   **Backend Framework:** Django
    
*   **Frontend:** HTML, CSS (Bootstrap)
    
*   **Template Engine:** Jinja
    

Models
------

The application uses a single Django model, **Recipe**, with the following fields:

*   **recipe\_name**: CharField (max length 100)
    
*   **recipe\_description**: TextField
    
*   **recipe\_image**: ImageField
    

Views
-----

The application's functionality is handled through three main views:

*   **recipes**: Displays and handles the addition of new recipes.
    
*   **update\_recipe**: Handles updating existing recipes.
    
*   **delete\_recipe**: Allows for the deletion of recipes.
    

URLs
----

The application uses the following URL patterns:

*   **recipes/**: Main page for displaying and adding recipes.
    
*   **update\_recipe//**: Endpoint for updating a specific recipe.
    
*   **delete\_recipe//**: Endpoint for deleting a specific recipe.
    

Templates
---------

Two HTML templates are used:

*   **base.html**: The base template including the necessary Bootstrap links.
    
*   **recipe.html**: Extends **base.html** and contains the form for adding/updating recipes and the table for displaying them.
    

Setup and Installation
----------------------

### Prerequisites

Before setting up the project, ensure you have Python installed on your system.

### Setting up a Virtual Environment

#### For Windows

1.  Open Command Prompt.
    
2.  Navigate to your project directory: **cd path\\to\\your\\project**.
    
3.  Create a virtual environment: **python -m venv env**.
    
4.  Activate the virtual environment: **.\\env\\Scripts\\activate**.
    
5.  Once activated, your prompt will change to indicate that you are now working inside **env**.
    

#### For Linux

1.  Open Terminal.
    
2.  Navigate to your project directory: **cd path/to/your/project**.
    
3.  Create a virtual environment: **python3 -m venv env**.
    
4.  Activate the virtual environment: **source env/bin/activate**.
    
5.  Once activated, your prompt will change to indicate that you are now working inside **env**.
    

### Installing Dependencies

With the virtual environment activated, install the required dependencies:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepip install -r requirements.txt   `

### Running the Application

1.  Run the Django migrations: **python manage.py migrate**.
    
2.  Start the Django development server: **python manage.py runserver**.
    
3.  Open a web browser and navigate to **http://127.0.0.1:8000/** to view the application.