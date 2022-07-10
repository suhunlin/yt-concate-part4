from pytube import YouTube

from yt_concate.settings import VIDEOS_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, utils, data, inputs):
        print('未過濾前共：', len(data), '筆資料!!')
        yt_set = set([found.yt for found in data])
        print('過濾完剩餘:', len(yt_set), '筆資料!!')

        for yt in yt_set:
            if utils.check_video_file_exists(yt):
                print(yt.caption_id + '.mp4 file exists!!!')
                continue
            print('downloading :', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.caption_id + '.mp4')

        return data




