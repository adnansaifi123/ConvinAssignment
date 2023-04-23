# views.py

from django.views import View
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView

CREDENTIALS_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

class GoogleCalendarInitView(APIView):
    def get(self, request):

        flow = Flow.from_client_secrets_file(
            os.path.join(CREDENTIALS_FILE),
            scopes=SCOPES,
            redirect_uri=request.build_absolute_uri('/rest/v1/calendar/redirect/')
        )

        # Generate authorization URL
        auth_url, _ = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )

        # Redirect to authorization URL
        return HttpResponseRedirect(auth_url)

class GoogleCalendarRedirectView(View):
    def get(self,request):
        flow = Flow.from_client_secrets_file(
            os.path.join(CREDENTIALS_FILE),
            scopes=SCOPES,
            redirect_uri=request.build_absolute_uri('/rest/v1/calendar/redirect/')
        )

        # Exchange authorization code for access token
        flow.fetch_token(code=request.GET.get('code'))
        credentials = flow.credentials

        service = build('calendar', 'v3', credentials=credentials)


        # Uncomment to add the event in calendar
        # event = {
        #     'summary': 'CONVIN 2023 MEET',
        #     'location': 'BHIVE WORKSPACE NO.112,AKR TECHPARK, A-BLOCK, 7TH MILE HOSUR ROAD, KRISHNA REDDY, INDUSTRIAL AREA,BENGALURU-560068',
        #     'description': 'A chance to hear more about CONVIN\'s products.',
        #     'start': {
        #         'dateTime': '2023-05-28T09:00:00-07:00',
        #         'timeZone': 'Asia/Kolkata',
        #     },
        #     'end': {
        #         'dateTime': '2023-05-28T17:00:00-07:00',
        #         'timeZone': 'Asia/Kolkata',
        #     },
        # }
        #
        # event = service.events().insert(calendarId='primary', body=event).execute()
        # link=event.get('htmlLink')
        # print(f'Event created:{link}')


        # Get the list of events from the user's calendar
        events_list = service.events().list(calendarId='primary',
                                            timeMin='2023-01-01T00:00:00Z',
                                            timeMax='2023-12-31T23:59:59Z',
                                            singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_list.get('items', [])
        print(events)
        if not events:
            return HttpResponse('No events found in calendar.')
        else:
            return HttpResponse(f'Events: {events}')