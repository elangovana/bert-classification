class BaseDatasetFactory:
    def get_dataset(self, data=None, preprocessor=None):
        raise NotImplementedError

    def get_label_mapper(self, data=None, preprocessor=None):
        raise NotImplementedError
