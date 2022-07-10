from .step import Step


class ReadCaptions(Step):
    def process(self, utils, data, inputs):
        for yt in data:
            captions = {}
            time_line = False
            caption = None
            time = None
            if not utils.check_caption_file_exists(yt):
                print(yt.caption_id + '.txt file not exists!!!!')
                continue

            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        time_line = False
                        caption = line.strip()
                        captions[caption] = time
            yt.captions = captions
        # for yt in data:
        #     print(yt.captions)
        return data




