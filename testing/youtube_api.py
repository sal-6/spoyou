# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import pprint

scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]


def get_authenticated_service():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "../creds/oauth.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    return youtube


def test():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "../creds/oauth.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()

    print(response)


def create_playlist(playlistName, desc="Description"):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "../creds/oauth.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playlistName,
            "description": desc,
            "tags": [
              "sample playlist",
              "API call"
            ],
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
    return response


def add_video_to_playlist(videoID,playlistID):
    youtube = get_authenticated_service() #write it yourself
    add_video_request=youtube.playlistItems().insert(
        part="snippet",
        body={
                'snippet': {
                  'playlistId': playlistID, 
                  'resourceId': {
                          'kind': 'youtube#video',
                      'videoId': videoID
                    }
                #'position': 0
                }
        }
    ).execute()

    return add_video_request


def search_for_video(query):
    youtube = get_authenticated_service() #write it yourself

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=query
    )
    response = request.execute()

    return response

if __name__ == "__main__":
    #res = create_playlist("Test Playlist")
    #add_video_to_playlist("BxagcXMdMS8", "PLKdfYrvfvONm--ZAkL_r7AKN7z75U3F0a")
    #pprint.pprint(search_for_video("hate myself nf"))