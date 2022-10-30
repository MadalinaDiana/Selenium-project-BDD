# Gerkin project
This project tests three types of pages, in chrome. The POM structure is used for a better organization of the files.
## Create project
Create new project in PyCharm, with virtualenv allocated.

### Pre-requisites
Install with pip install <library name>
- behave
- behave-html-formatter
- selenium
- webdriver-manager
## Folder and file structure
```bash
/features
    /pages # here we have defined the methods used
              # in the testing steps
        /base_page.py
        /complete_signup.py
        /form_page.py
        /verify_url.py
    /steps #here we implement steps to be executed,
            # using the methods defined in pages
        /complete_signup.py 
        /form_page.py
        /verify_url.py
    /browser.py #here is where test execution is initialized
    /complete_signup.feature #here are the tests in Gherkin language
    /environment.py #here we set hooks that put the browser in context
    /form_error.feature
    /verify_url.feature
/behave.ini
```