import glob
import json
import os

from kkbox_developer_sdk.api import KKBOXAPI
from kkbox_developer_sdk.auth_flow import KKBOXOAuth

from pytube import Search, YouTube

# read CLIENT_ID and CLIENT_SECRET from secret.json
CLIENT_ID = json.load(open("secret.json"))["CLIENT_ID"]
CLIENT_SECRET = json.load(open("secret.json"))["CLIENT_SECRET"]
auth = KKBOXOAuth(CLIENT_ID, CLIENT_SECRET)
token = auth.fetch_access_token_by_client_credentials()
kkboxapi = KKBOXAPI(token)


def get_singers(file_name):
    singers = []
    with open(file_name, "r", encoding="UTF-8") as f:
        line = f.readline()
        while line:
            singers.append(line.strip())
            line = f.readline()

    return singers


def get_singer_id(name):
    result = kkboxapi.search_fetcher.search(name, types=["artist"])
    return result["artists"]["data"][0]["id"]


def get_top_track_from_id(singer_id="KnECoRl82J54gSwkat"):
    result = kkboxapi.artist_fetcher.fetch_top_tracks_of_artist(singer_id)
    return result["data"]


def download_mp3_from_tracks(tracks, target_path="Downloads/"):
    for track in tracks:
        song_name = track["name"]
        singer = track["album"]["artist"]["name"]
        s = Search("{} {}".format(song_name, singer))

        try:
            yt = s.results[0]
            video = yt.streams.filter(only_audio=True).first()
        except:
            print("!!! fail to dowaload {} {}".format(song_name, singer))
            continue
        out_file = video.download(output_path=target_path)
        new_path = change_file_name(out_file)

        print(os.path.basename(new_path) + " has been successfully downloaded.")


def change_file_name(file_name):
    directory = os.path.dirname(file_name)  # 获取目录部分
    filename = os.path.basename(file_name)  # 获取文件名部分

    # 获取当前文件夹中的所有文件
    mp3_files = glob.glob(os.path.join(directory, "*.mp3"))
    # 计算文件数量
    mp3_file_count = len(mp3_files)
    name_without_ext = os.path.splitext(filename)[0]
    # 构建新的文件名
    new_filename = f"{mp3_file_count+1:02d}_{name_without_ext}.mp3"

    # 构建新的文件路径
    new_path = os.path.join(directory, new_filename)
    os.rename(file_name, new_path)
    return new_path


if __name__ == "__main__":
    singers = get_singers("test_singers.txt")
    for name in singers:
        singer_id = get_singer_id(name)
        tracks = get_top_track_from_id(singer_id)
        print(f"Start Downloading {name}'s {len(tracks)} songs ...")
        download_mp3_from_tracks(tracks)
