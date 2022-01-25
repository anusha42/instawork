Application structure: 
The application is titled fullStackTakeHome, within the application:

	-listMembers contains the functionality for the home page of the application, it features the information 
	of all team members, and a count. Also allows you to either click to add or edit a team member.

	-addMember contains functionality for adding a team member. It allows the user to to input information for all of the team members, and choose their roles. 

	-editMember folder contains functionality for editing the information of a team member or deleting a team member. 


How to run the application: 
To run the app cd/address into the appropriate folder (./instawork/fullStackTakeHome/fullStackTakeHome) and run the following command: python manage.py runserver


How to open application: 
After starting the development server navigate to http://127.0.0.1:8000/home/ (the home page that features the list of the team members)


Application Functionality: 
After navigating to the home page (http://127.0.0.1:8000/home/ ), double click on a team member to edit their information. Click the add button to add a team member. 

When editing a team member you cannot change their email as it is their primary key in the database, in addition, if you attempt to make this change your edit will not save. 

When adding a team member, the phone number must be 9 digits (or shorter) of the form XXXXXXXXXX