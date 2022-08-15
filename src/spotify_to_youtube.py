
from pprint import pprint

import utils.spotify as sp
import utils.youtube as yt
import utils.general as gl

def transfer_spotify_saves_to_youtube(start_offset=0):

    res = yt.create_playlist("Liked Songs", "Programmatically Generated playlist of saved Spotify songs.")
    playlist_id = res["id"]

    songs = sp.get_user_liked_songs()

    for idx, item in enumerate(songs):
        
        try: 
            search_res = yt.search_for_video(f"{item['name']} {item['artist']}")
            vid_id = search_res["items"][0]["id"]["videoId"]

            yt.add_video_to_playlist(vid_id, playlist_id)

            gl.printProgressBar(idx + 1, len(songs), prefix="Progress", suffix="Complete", length=50)
        except:
            print("Error at index", idx)


if __name__ == "__main__":
     transfer_spotify_saves_to_youtube()