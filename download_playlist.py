import os
import re
from argparse import ArgumentParser

import main
from pytube import Playlist

parser = ArgumentParser()
parser.add_argument("-i", "--list_id", help="The playlist id", required=True)
parser.add_argument("-p", "--target_path", help="The target path name")


def convert_to_valid_path(string):
    invalid_chars = r'[\\/:\*\?"<>\|\s]'  # 不適合當路徑的特殊符號
    return re.sub(invalid_chars, "_", string)


if __name__ == "__main__":
    args = parser.parse_args()
    pl = Playlist(f"https://www.youtube.com/playlist?list={args.list_id}")
    target_path = args.target_path or pl.title
    valid_path = convert_to_valid_path(target_path)
    print(f"Start downloading platlist: {pl.title} with {len(pl.videos)} songs")

    for vid in pl.videos:
        try:
            audio = vid.streams.filter(only_audio=True).first()
            out_file = audio.download(output_path=valid_path)
            new_path = main.change_file_name(out_file)
            print(os.path.basename(new_path) + " has been successfully downloaded.")
        except:
            print(f"!!! Fail to download {vid.title}-{vid.author}")
            continue
        pass
