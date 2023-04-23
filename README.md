# ConvinAssignment

Steps:
1. Run the Command: 'pip install -r requirements.txt'

2. Run the command: 'python manage.py runserver'

<img width="445" alt="image" src="https://user-images.githubusercontent.com/67619920/233850240-81b80df7-9991-44ae-a100-8bd315c03a83.png">

3. Click on the url

<img width="779" alt="image" src="https://user-images.githubusercontent.com/67619920/233851209-3ae159d4-29c0-4bc5-a934-2ab7368dac79.png">

4. Now add the API's end point to url e.g,

url='http://127.0.0.1:8000/'

Api details:
  ^admin/
  ^ ^rest/v1/calendar/init/ [name='GoogleCalendarInitView']
  ^ ^rest/v1/calendar/redirect/ [name='GoogleCalendarRedirectView']

Then url should be url= 'http://127.0.0.1:8000/rest/v1/calendar/init/'   ->  This will call GoogleCalendarInitView()
<img width="449" alt="image" src="https://user-images.githubusercontent.com/67619920/233851409-3980a1d8-dbb9-4813-86c5-e88ec8146a68.png">
<img width="393" alt="image" src="https://user-images.githubusercontent.com/67619920/233851431-c39ab0be-42a6-4842-ad63-db3fff6708b2.png">

Credentials:
user1CalendarTesting@gmail.com

Password:user1testing

<img width="383" alt="image" src="https://user-images.githubusercontent.com/67619920/233851466-233c3c74-06a0-4f32-b28d-83b773518623.png">
Click on Continue

<img width="296" alt="image" src="https://user-images.githubusercontent.com/67619920/233851490-8810729f-c850-4006-9f82-9270df4f6a07.png">

Give access to the Account, Click on Continue

Now it will be redirected to another Api ---> ^rest/v1/calendar/redirect/ [name='GoogleCalendarRedirectView']
and it will return all the events in the calendar.

<img width="955" alt="image" src="https://user-images.githubusercontent.com/67619920/233851608-fcdd329f-0aca-4fbc-adf6-b62fba2ea0de.png">
