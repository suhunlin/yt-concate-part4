from yt_concate.models.found import Found
from .step import Step


class Search(Step):
    def process(self, utils, data, inputs):
        found = []
        search_word = inputs['search_word']
        for yt in data:
            if not utils.check_caption_file_exists(yt):
                print(yt.caption_id + '.txt file is not exists!!!')
                continue
            captions = yt.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        # for fd in found:
        #     print(fd.yt, fd.time, fd.caption)
        return found
