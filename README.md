searchconsole - Python Library for Google Search Console API

# Introduction

searchconsole is a Python library that provides an easy-to-use interface for working with the Google Search Console API. With this library, you can fetch data from your Search Console account and use it to analyze your website's performance in search results.

# Getting Started

Before you can use the searchconsole library, you need to generate a credentials.json file that will allow you to authenticate with the Google Search Console API. To generate this file, you can use the Credential class provided by the library.
```python
from credential.credential import Crediential

client_id = "kjahfdnjkeahfnulkjbn38294u2389"
client_secret = "32u4393kjbjjk3b4bk331094i3jb"

# create the credentials.json file in your home directory

Credential(client_id=client_id, client_secret=client_secret)

# they will send you a new tab where you can allow the permission and get the key

# Enter your Authorization code here:-

```
 After enter the Authorization you will get the credenial.json then after comment the Credential(client_id=client_id, client_secret=client_secret)
 
 

This will create a credentials.json file in your home directory that you can use to authenticate with the API.



Make sure that you have obtained the credentials.json file. Please note that the refresh token for this library expires after 6 months of inactivity. If you use the library before the expiration date, the expiration time gets extended to another 6 months.

So you don't need to generate the credential.json again and again

# Fetching Data

Once you have generated your credentials.json file, you can use the searchconsole library to fetch data from your Search Console account. Here is an example of how to fetch search analytics data for a given domain:
```python
from searchconsole.searchconsole import Searchconsole

domain = "https://www.example.com/"
start_date = "2022-01-01"


# dont write end date they will automatically update as date.today()

authenticate with the API using credentials.json

auth_response = SearchConsole(domain=domain,start_date=start_date, credentials='credentials.json')

# print the data

# print(auth_response)

report_dict = []
for i in auth_response['rows']:
    auth_data = i
    new_dict = {
        "query": auth_data["keys"][0],
        "page": auth_data["keys"][1],
        "country": auth_data["keys"][2],
        "device": auth_data["keys"][3],
        "date": auth_data["keys"][4],
        "clicks": auth_data["clicks"],
        "impressions": auth_data["impressions"],
        "ctr": auth_data["ctr"],
        "position": auth_data["position"]
    }
    report_dict.append(new_dict)
print(report_dict)

```

# Output:


["query", "page", "country", "device", "date","impression","clicks","position","ctr"]
```python
{
"query":"console",
"country":"ind",
"page":"www.example.com",
"device":"Desktop",
"date":"2023-02-13",
"impression":"23",
"clicks":"23",
"position":"2",
"ctr":"2",
}

```

# Requirements

The following dependencies are required to use the searchconsole library:

apiclient
oauth2client
google-api-python-client
httplib2

You can add these requirements to a file called requirements.txt in the root directory of your library, with each requirement on a new line. This will make it easy for users to install all necessary dependencies by running pip install -r requirements.txt.

# Unit Testing

The searchconsole library comes with a large and growing set of unit tests to ensure its functionality is working correctly. These unit tests can be found in the tests directory of the library. By running the tests, you can ensure that the library is functioning correctly and catch any errors that may arise.

# Conclusion

With the searchconsole library, it is easy to fetch data from your Google Search Console account and use it to analyze your website's performance in search results. By following the steps outlined in this document, you can quickly get started with the library and begin using it to improve your website's search performance.
