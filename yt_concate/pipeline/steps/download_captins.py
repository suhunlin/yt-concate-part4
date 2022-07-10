from pytube import YouTube

from .step import Step


class DownloadCaptions(Step):
    def process(self, utils, data, inputs):
        for yt in data:
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError) as e:
                print(__name__, 'Dwonload caption:', yt.caption_id + '.txt Error', e)
                continue

            # save the caption to a file named Output.txt
            text_file = open(yt.get_caption_filepath(), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data
