Steps to Execute the task

Download the files in the repository

Install Xampp in your machine and make sure that Apache and SQL is working fine

Once the Xampp is installed open the xampp control panel (press win button and search for Xampp control panel and double click on it)

Once the Xampp is opened then start Apache and SQL service 

Now, Click on the Admin button in SQL and wait till the PHPMyAdmin page opens where you can find the databases in your laptop/PC.

Once the page is loaded select the import option on the middle of the pane and go to the place where you have downloaded the repository files

Select the file named as “task.sql” and click on import

Once this process is finished you can find the task database with four tables named as “Account” , “Application” , “Course” , “TermCourseRegistrationApplication” with 2 rows of data added to each table.

Once you have imported the database to the Xampp , check whether the python libraries required to execute the task are present in your laptop. 
	
	Python Installation:
	
Download the Installer:
Go to the official Python website.
Download the latest Python installer for Windows (.exe file).
Run the Installer:
Double-click the downloaded file to start the installation.
On the installer screen, check "Add Python to PATH" at the bottom.
Click "Install Now" to install Python with default settings.
Verify Installation:
Open Command Prompt (type cmd in the Start Menu).
	python --version
You should see the installed Python version. If so, Python is installed successfully!
Environment
Install pip (Python Package Manager)
pip usually comes installed with Python 3, but you can verify by running:
	pip3 --version

	
The libraries required to execute the task are as follows:
Pymysql -> pip install pymysql
Pandas -> pip install pandas
Sqlalchemy -> pip install sqlalchemy
Mysql connector -> pip install mysql-connector-python

Once all the libraries are installed , open the python idle and go to file and select open and go to the downloaded repository place and selected the “updated-task.py” file and click on run 

It will give the output as follows :

       Program                 Email  ... Fee_Details Application_Status
0  Engineering  student1@example.com  ...       200.0           Accepted
1      Science  student2@example.com  ...       250.0            Pending

[2 rows x 7 columns]


