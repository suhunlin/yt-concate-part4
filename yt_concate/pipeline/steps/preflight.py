from .step import Step


class Preflight(Step):
    def process(self, utils, data, inputs):
        utils.create_dir()
