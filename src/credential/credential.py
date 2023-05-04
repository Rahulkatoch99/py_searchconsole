from oauth2client.client import OAuth2WebServerFlow
import webbrowser
import json


def Crediential(client_id, client_secret):
    OAUTH_SCOPE = "https://www.googleapis.com/auth/webmasters"
    Redirect_url = 'urn:ietf:wg:oauth:2.0:oob'
    flow = OAuth2WebServerFlow(
        client_id, client_secret, OAUTH_SCOPE, Redirect_url)
    auth_url = flow.step1_get_authorize_url()
    webbrowser.open_new_tab(auth_url)
    auth_code = input("Enter your Authorization code here:-").strip()
    credentials = flow.step2_exchange(auth_code)
    access_Token = credentials.access_token
    refresh_Token = credentials.refresh_token
    expire_time = credentials.token_expiry
    token_uri = credentials.token_uri
    id_token = credentials.id_token
    id_token_jwt = credentials.id_token_jwt
    token_response = credentials.token_response
    token_response_access_token = token_response['access_token']
    token_response_expires_in = token_response['expires_in']
    token_response_scope = token_response['scope']
    token_response_token_type = token_response['token_type']
    scopes = credentials.scopes
    token_info_uri = credentials.token_info_uri
    invalid = credentials.invalid
    credential_json = {"access_token": access_Token, "client_id": client_id, "client_secret": client_secret, "refresh_token": refresh_Token, "token_expiry": f"'{expire_time}'", "token_uri": token_uri, "user_agent": "None", "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": id_token, "id_token_jwt": id_token_jwt, "token_response": {"access_token": token_response_access_token,
                                                                                                                                                                                                                                                                                                                                                            "expires_in": token_response_expires_in, "scope": token_response_scope, "token_type": token_response_token_type}, "scopes": scopes, "token_info_uri": token_info_uri, "invalid": invalid, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}
    jsonString = json.dumps(credential_json, default=str)
    jsonFile = open("credentials.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
