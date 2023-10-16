REALLY ONLY INTERESTED IN HELP WITH MANAGE DATABASE LIVE:
Managing, manage little, e 

PRIOR HISTORY:

USED ONCE A MONTH OR EVERY COUPLE OF WEEKS 

HEALTHCARE PROVIDERS BILL SERVICES:
- Analysis for REVENUE and PAYMENTS
-- Organizing Client Payments 
--- For example blue cross blue shield sends

DROP DOWN FILTERS AS REPORTED DATABASE
MANUEL feedback loop table shows what has already changed.



POWERVI Deskboard:
?? WHAT THE FUCK IS POWERVI ?? 
-- Creates Visuals ... Presents Data
--- Client Logs in



Company Founder: Jeff Fischer
Developer:  Anthony Guzzardo

Web Framework: 
- Utilizes Flask Framework
- Goal is fast Prototype

Backend: 
- Client Data is Refreshed Nightly (Once Daily)
-- HOW?? Database Software probably mysql

Frontend: 
- Client Accesses As is Data
- Drop Down Filter let's them select what 
inputs they are making.
- Calculations are obviously already done for them, 
maybe there is customization there.

Product:
- Essentially a watered down final table is the final
product.


Flask: 
- Lightweight micro framework used for big or small webapps. 
Not much built in functionally, have to design most of the 
infrustracture yourself.

Flask Setup:

1. First we imported the Flask class. An instance of this 
class will be our WSGI application.

2. Next we create an instance of this class. 
The first argument is the name of the application’s 
module or package. __name__ is a convenient 
shortcut for this that is appropriate for most cases. 
This is needed so that Flask knows where to look for 
resources such as templates and static files.

3.We then use the route() decorator to tell 
Flask what URL should trigger our function.

4. The function returns the message we want to 
display in the user’s browser. The default 
content type is HTML, so HTML in the string 
will be rendered by the browser.

Project Structure:
- Python 3 
- Flask web Framework -- version 2.3.3 (python -c "import flask; print(flask.__version__)")
- SQlite

ABOUT FLASK: 
- Uses Jinja template engine to dynamically build HTML pages using familiar 
Python concepts and objects.

LOGIC FOR RENDERING TABLES IS SERIOUSLY OFF. Have to click multiple buttons multiple times for GET