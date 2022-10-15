### Requirements:
 - Python3  
### Instructions(In Terminal):  
```python  
virtualenv venv  
source ./venv/bin/activate
pip install -r requirements.txt  
django-admin startproject task1  
cd task1  
python manage.py runserver  
python manage.py startapp first  
```
### Tasks Completed :
Successfully setup a Login,Register Page and The SuperUser with access to banning users/CRUD tasks with SQLite as the Database.  
***Also the User Can fill a maximum of only One CLUB based on his/her interest based on an attractive page with info of all clubs
as well as videos attached with them.***  
Added Dashboard for a User wherein the user can view all the tasks attached to his/her club and ***has access to delete as well as edit only his/her task also can see only his/her subtasks*** along with the deadline,social media platform set,submitting assignment.  
ONLY AFTER FILLING THE FOLLOWING PAGE CAN the ***LOGGEDINUSER*** VIEW TASKS IN HIS/HER CLUB:
these were taken at 67% zoom to ensure the ui visible
![Screenshot (97)](https://user-images.githubusercontent.com/101446457/195915576-7427be7a-e67d-42cf-a1c3-634e5c34bc95.png)
![Screenshot (98)](https://user-images.githubusercontent.com/101446457/195915585-d1fe6fcd-81ef-494a-8da9-0ff3a1f6e14e.png)
![Screenshot (99)](https://user-images.githubusercontent.com/101446457/195915592-3d56cd1a-47de-4b0b-b1ed-b6d67b7eda00.png)
VIEW TASKS(similar UI used to view subtasks but it has additional features as it is visible in models.py):  
![VIEW TASKS)](https://user-images.githubusercontent.com/101446457/195985418-02262a7a-b3b8-4af9-ab96-d3fcec6c5953.png)  
ADD TASKS(similar UI used to view subtasks but it has additional features as it is visible in models.py):  
![ADD TASKS](https://user-images.githubusercontent.com/101446457/195985597-894bdf15-6ba9-44f3-8652-546e4f04937d.png)  
IT IS RESPONSIVE WEB APP!  
### References used:  
-[bootstrap]https://getbootstrap.com/docs/5.2/getting-started/introduction/  
-[documentation](https://docs.djangoproject.com/en/4.0/)  
 ### UNIMPLEMENTED:  
 ***WASN'T ABLE TO INTEGRATE GOOGLE DRIVE AND CALENDAR API'S.***
 
 





