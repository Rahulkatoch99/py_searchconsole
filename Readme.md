searchconsole - Python Library for Google Search Console API

Introduction

searchconsole is a Python library that provides an easy-to-use interface for working with the Google Search Console API. With this library, you can fetch data from your Search Console account and use it to analyze your website's performance in search results.

Getting Started

Before you can use the searchconsole library, you need to generate a credentials.json file that will allow you to authenticate with the Google Search Console API. To generate this file, you can use the Credential class provided by the library.

from searchconsole.credential import Credential

client_id = "kjahfdnjkeahfnulkjbn38294u2389"
client_secret = "32u4393kjbjjk3b4bk331094i3jb"

# create the credentials.json file in your home directory

Credential(client_id=client_id, client_secret=client_secret)

# they will send you a new tab where you can allow the permission and get the key

Enter your Authorization code here:-

# After enter the Authorization you will get the credenial.json then after comment the Credential(client_id=client_id, client_secret=client_secret)

This will create a credentials.json file in your home directory that you can use to authenticate with the API.

Fetching Data
Once you have generated your credentials.json file, you can use the searchconsole library to fetch data from your Search Console account. Here is an example of how to fetch search analytics data for a given domain:

from searchconsole import SearchConsole

domain = "example.com"
start_date = "2022-01-01"
end_date = "2022-01-31"

# authenticate with the API using credentials.json

data = SearchConsole(domain, credentials='credentials.json')

# print the data

print(data)

# Output:

# ["query", "page", "country", "device", "date","impression","clicks","position","ctr"]

Requirements
The following dependencies are required to use the searchconsole library:

apiclient
oauth2client
google-api-python-client
httplib2
You can add these requirements to a file called requirements.txt in the root directory of your library, with each requirement on a new line. This will make it easy for users to install all necessary dependencies by running pip install -r requirements.txt.

Unit Testing
The searchconsole library comes with a large and growing set of unit tests to ensure its functionality is working correctly. These unit tests can be found in the tests directory of the library. By running the tests, you can ensure that the library is functioning correctly and catch any errors that may arise.

Conclusion
With the searchconsole library, it is easy to fetch data from your Google Search Console account and use it to analyze your website's performance in search results. By following the steps outlined in this document, you can quickly get started with the library and begin using it to improve your website's search performance.
