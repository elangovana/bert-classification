
from datasets.base_dataset_factory import BaseDatasetFactory
from datasets.sst2_dataset import SST2Dataset
from datasets.sst2_label_mapper import SST2LabelMapper


class SST2DatasetFactory(BaseDatasetFactory):

    def get_dataset(self, data=None, preprocessor=None):
        return SST2Dataset(data, preprocessor, label_mapper=self.get_label_mapper())

    def get_label_mapper(self, data=None, preprocessor=None):
        return SST2LabelMapper()
