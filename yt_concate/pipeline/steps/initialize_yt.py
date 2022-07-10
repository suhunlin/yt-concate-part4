from yt_concate.models.yt import YT
from .step import Step


class InitializeYT(Step):
    def process(self, utils, data, inputs):
        return [YT(url) for url in data]
