
# Daily Stock Update (Web Scrape)

In this project we have will get top 10 stocks from Nifty 500 and send email. Automatically execute the code if we set




## Screenshot

![App Screenshot](https://bestintechnology.in/uploadLinks/daily_stock_update.PNG)


## Create App Password (Gmail Account)

To create an app password for your Gmail account, please follow these steps:

- Log in to your Gmail account.
- Click on your profile picture in the top right corner and select "Google Account".
- Click on "Security" on the left-hand side menu.
- Scroll down to "Signing in to Google" and click on "App passwords".
- Select the app and device you want to generate the app password for.
- Follow the instructions on the screen to generate the app password.

Use the app password instead of your regular password when prompted by the app or device.


## Create Scheduler in Your system (For Auto Alert)
You can execute code manually at any time. But if you want to execute the python code automatically at certain time in a day. If you don't want to schdule task then steps not required. 

To execute this code daily at 4 PM, you can use a task scheduling system provided by your operating system. Here's an example of how to schedule this script to run daily at 4 PM using the built-in Windows Task Scheduler on a Windows 10 computer:

- Open the Task Scheduler by pressing the Windows key + R, typing "taskschd.msc" in the Run dialog box, and pressing Enter.
- Click on "Create Task" in the "Actions" pane on the right-hand side.
- In the "General" tab, give your task a name and a description (optional).
- In the "Triggers" tab, click "New" to create a new trigger. Set the trigger to run "Daily" at 4:00 PM, and choose the start date and time.
- In the "Actions" tab, click "New" to create a new action. Set the action to "Start a program", and browse to the location of your Python executable (e.g., C:\Python39\python.exe).
- In the "Add arguments" field, enter the full path to your Python script that you want to execute at 4:00 PM daily. For example: "C:\path\to\your\script.py".
- In the "Conditions" tab, you can set any additional conditions for the task to run, such as only when the computer is plugged in, or only if a certain amount of idle time has passed.
- Click "OK" to create the task.
- Your task should now appear in the list of tasks in the Task Scheduler. You can right-click on it and choose "Run" to test it out, or wait until 4:00 PM to see if it runs automatically.



## Tech Stack

**Libraries:** BeautifulSoup, requests, datetime, SMTP_SSL, EmailMessage, pandas, build_table

**Note:- The code used in this project is only for the educational purpose.**

