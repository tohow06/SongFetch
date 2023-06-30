from pytube import Playlist
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-u", "url", help="The playlist url")
parser.add_argument("-p", "target_path", help="The target path name")


if __name__ == "__main__":
    # read user arg --url="https://www.youtube.com/playlist?list=PL3OrA2XJoWPnkzeA8WH0-aBhd0_KzZKXP"
    args = parser.parse_args()
    pl = Playlist(args.url)
    for vid in pl.videos:
        audio = vid.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path=args.target_path)
        pass
