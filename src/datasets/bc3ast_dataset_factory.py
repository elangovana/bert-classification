from datasets.base_dataset_factory import BaseDatasetFactory
from datasets.bc3ast_dataset import BC3ASTDataset
from datasets.bc3ast_label_mapper import BC3ASTLabelMapper


class BC3ASTDatasetFactory(BaseDatasetFactory):

    def get_dataset(self, data=None, preprocessor=None):
        return BC3ASTDataset(data, preprocessor, label_mapper=self.get_label_mapper())

    def get_label_mapper(self, data=None, preprocessor=None):
        return BC3ASTLabelMapper()
