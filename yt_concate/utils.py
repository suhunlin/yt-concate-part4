import os

from settings import DOWNLOADS_DIR
from settings import VIDEOS_DIR
from settings import CAPTIONS_DIR


class Utils:
    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def check_video_list_file_exists(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def check_caption_file_exists(self, yt):
        filepath = yt.get_caption_filepath()
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def check_video_file_exists(self, yt):
        return os.path.exists(yt.video_filepath) and os.path.getsize(yt.video_filepath) > 0
