# Sample Flask App to print headers and return remote username
Use this sample application code in CML to view request headers and demonstrate Remote-User detection.

This is a basic deomnstration of how CML username is added to headers when a user accesses a CML application while authenticated.

## Deploy
- Clone this git repo into a CML project
- Create a CML Application in the project
   - Pick a subdomain ex(flask-headers-app)
   - Set script (flask-headers.py)
   - Pick Runtime (suggest Workbench Python3.9)
- Navigate to application url in a browser 
  - Remote-user will be displayed if Application authentication was not disabled for this Application
  - Other headers are printed in Application logs for reference

