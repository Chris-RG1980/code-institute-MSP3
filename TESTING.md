# Muscle Metrics - Testing
![image](resources/mockup.png)
***
**Contents**
- [Muscle Metrics - Testing](#muscle-metrics---testing)
  - [Responsiveness](#responsiveness)
    - [Mobile Screenshots](#mobile-screenshots)
    - [Tablet Screenshots](#tablet-screenshots)
    - [Desktop Screenshots](#desktop-screenshots)
    - [Summary](#summary)
  - [Automated Testing](#automated-testing)
    - [W3C Validator](#w3c-validator)
    - [JSHint](#jshint)
    - [Python Linter](#python-linter)
    - [Validation Summary](#validation-summary)
    - [Lighthouse](#lighthouse)
    - [Wave](#wave)
  - [Browser Compatibility](#browser-compatibility)


***
## Responsiveness
This website has been tested on a wide range of screen sizes from various manufacturers to account for the differences between them. It’s crucial to test website responsiveness due to the web being mostly accessed using mobile devices. A responsive website guarantees a uniform user experience across different screen sizes and resolutions, making it easy for visitors to access and navigate the site, regardless of the device they’re using. Additionally, responsive design enhances search engine optimization (SEO), as search engines prioritize mobile-friendly sites in their rankings. The testing has been carried out using the device list on the chrome developer tools.

The resolutions tested as as follows:                        
Galaxy S III: 360 x 640                               
Iphone SE: 375 x 667                                  
Iphone 12 Pro: 390 x 844                           
Moto G Power: 412 x 823                                                             
Ipad Air: 768 x 1024                                                                
Nexus 10: 800 x 1280                                                                
Desktop 1080p: 1920 x 1080   

### Mobile Screenshots
![image](resources/responsive/mobile_screenshots.PNG)           
### Tablet Screenshots
![image](resources/responsive/tablet_screenshots.PNG)    
### Desktop Screenshots
![image](resources/responsive/desktop_screenshots1.PNG)            
![image](resources/responsive/desktop_screenshots2.PNG)            
![image](resources/responsive/desktop_screenshots3.PNG)           
![image](resources/responsive/desktop_screenshots4.PNG)        
### Summary
![image](resources/responsive/summary.PNG)                 

***
## Automated Testing


### W3C Validator
Testing has been completed using the W3C code validators to ensure that the code used is clean, consistent and adheres to best practices. No warnings or errors were found and the results can be found below. The W3C Markup Validation Service is unable to validate the profile page as it contains content that is only accessible after logging in.          

1. [Home Page Validation](resources/validation/home%20_page.PNG)    
2. [Login Page Validation](resources/validation/login.PNG)                
3. [Registration Page Validation](resources/validation/register.PNG)             
4. [Exercise Log Validation](resources/validation/log_exercise.PNG)            
5. [Dashboard Validation](resources/validation/dashboard.PNG)                                    
6. [Profile Page](resources/validation/profile.PNG) *(Profile Page could not be validated)*                                
7. [CSS Validation](resources/validation/css.PNG)

### JSHint   
Quality testing of the JavaScript code has been carried out using [JSHint](https://jshint.com/). Before testing please ensure the checkboxes next to "New JavaScript features (ES6)" and "jQuery" have been turned on. To do this please click "CONFIGURE" and if needed click "New JavaScript features (ES6)" and "jQuery".                             

**_script.js_**    
![image](resources/validation/js.PNG)

### Python Linter      
The Code Institute Python Linter has been used to validate the python code. No errors were found and the results can be seen by clicking the links below.        

1. [muscle_metrics/app.py](resources/validation/python_linter/app.PNG)     
2. [muscle_metrics/routes.py](resources/validation/python_linter/routes.PNG)        
3. [muscle_metrics/seed_data.py](resources/validation/python_linter/seed_data.PNG)     
4. [muscle_metrics/init.py](resources/validation/python_linter/init.PNG)
5. [register/routes.py](resources/validation/python_linter/register_routes.PNG)     
6. [register/forms/registration.py](resources/validation/python_linter/registration_form.PNG)
7. [register/forms/init.py](resources/validation/python_linter/registration_form_init.PNG)
8. [profile/routes.py](resources/validation/python_linter/profile_routes.PNG)
9. [profile/forms/init.py](resources/validation/python_linter/profile_forms_init.PNG)
10. [profile/forms/change_password.py](resources/validation/python_linter/change_password.PNG)
11. [profile/forms/edit_email.py](resources/validation/python_linter/edit_email.PNG)
12. [profile/forms/edit_first_name.py](resources/validation/python_linter/edit_first_name.PNG)
13. [profile/forms/edit_last_name.py](resources/validation/python_linter/edit_last_name.PNG)
14. [models/users.py](resources/validation/python_linter/users.PNG)
15. [models/progress.py](resources/validation/python_linter/progress.PNG)
16. [models/muscle_groups.py](resources/validation/python_linter/muscle_group.PNG)
17. [models/exercises.py](resources/validation/python_linter/exercises.PNG)
18. [models/init,py](resources/validation//python_linter/models_init.PNG)
19. [login/routes.py](resources/validation/python_linter/login_routes.PNG)
20. [login/forms/login.py](resources/validation//python_linter/login.PNG)
21. [login/forms/init.py](resources/validation//python_linter/login_forms_init.PNG)
22. [home/routes.py](resources/validation/python_linter/home_routes.PNG)
23. [exercise_log/routes.py](resources/validation/python_linter/exercise_log_routes.PNG)
24. [exercise_log/forms/log.py](resources/validation/python_linter/exercise_log_forms_log.PNG)
25. [exercise_log/forms/init.py](resources/validation/python_linter/exercise_log_forms_init.PNG)
26. [dashboard/routes.py](resources/validation/python_linter/dashboard_routes.PNG)

### Validation Summary
![image](resources/validation/summary.PNG)

***
### Lighthouse
The lighthouse results can be found for each page below.    

![image](resources/validation/lighthouse_summary.PNG)   
***
### Wave
***
## Browser Compatibility
Testing has been carried out on the browsers within the below table as these browsers are most used, but in addition to this Firefox uses Gecko rendering engine while the others use WebKit. This helps identify any inconsistencies or rendering discrepancies that may arise due to variations in the rendering engines.        

![image](resources/validation/browser_testing.PNG)
***