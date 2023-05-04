import httplib2
from datetime import date
from googleapiclient.discovery import build
from oauth2client.client import OAuth2Credentials
import datetime


def execute_request(service, property_uri, request):
    """Executes a searchAnalytics.query request.
    Args:
      service: The searchconsole service to use when executing the query.
      property_uri: The site or app URI to request data for.
      request: The request to be executed.
    Returns:
      An array of response rows.
    """
    return service.searchanalytics().query(
        siteUrl=property_uri, body=request).execute()


def Searchconsole(domain, start_date,credentials_json):
    with open(credentials_json, 'r') as f:
        credentials = OAuth2Credentials.from_json(f.read())
    # # credentials = flow.step2_exchange(code)

        # Create an httplib2.Http object and authorize it with our credentials
        http = httplib2.Http()
        new_json_string = credentials.to_json()
        token_expiry_time = credentials.token_expiry
        current_date_time = datetime.datetime.now()
        formatted_time = current_date_time.strftime('%Y-%m-%d %H:%M:%S')
        if token_expiry_time == formatted_time:
            credentials.refresh(http)
        credentials.authorize(http)

        webmasters_service = build('searchconsole', 'v1', http=http)
        end_Date = date.today()

        request = {
            'startDate': f'{start_date}',
            'endDate': f'{end_Date}',
            'dimensions': ["query", "page", "country", "device", "date"], 'searchType': "Web",
            'rowLimit': 25000,
            'startRow': 1
        }

        return execute_request(
            webmasters_service, domain, request)
