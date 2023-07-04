This application was created to explore the many usages of Selenium. 

Files you will find:

 - app.py - performs a basic authentication login and password in this website: https://www.saucedemo.com/

 - otherapp.py - explores seven different websites to test a few tools that Selenium can offer, such as: clicking, accepting pop ups, dropdowns, refresh, drag and drop, hoover and press keys. https://the-internet.herokuapp.com/ 

To run this application on your machine follow these steps: 

- Create and activate a virtual environment: 
```
python3 -m venv venv
source venv/bin/activate
```
- Download Selenium and Webdriver Manager: 
```
pip install selenium
pip install webdriver-manager
```
- Run either file. It should open a Chrome browser, perform what's required and close the browser after it's finished.

PS: This application uses Chrome Webdriver, and it is installed the first time you run the program, depending on which version of Chrome
you have installed, it will download according. 