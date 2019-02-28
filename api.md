# PyDrive:
PyDrive is a wrapper library of google-api-python-client that simplifies many common Google Drive API tasks.
# Google Drive API:
The Google Drive Android API provides abstractions for managing file content and metadata. Files are represented by the DriveFile interface; folders by the DriveFolder interface.
### Installation
- To install PyDrive use the following command: ```$ pip install PyDrive```
- To install the current development version from GitHub, use: 
    ```$ pip install git+https://github.com/googledrive/PyDrive.git#egg=PyDrive```
### Authentication
- Drive API requires OAuth2.0 for authentication.
- PyDrive makes complex authentication process simple
- Create project in API Console
- Search 'Google Drive API' and Click 'Enable'
- Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’
- Now, the product name and consent screen need to be set -> click ‘Configure consent screen’
- Select ‘Application type’ to be Web application
- Enter an appropriate name
- Authorize JavaScript origins
- Authorized redirect URIs
- Click 'Save'
- Click ‘Download JSON’ on the right side of Client ID
### Initialization
```from pydrive.auth import GoogleAuth```
```gauth = GoogleAuth()```
```gauth.LocalWebserverAuth()```

