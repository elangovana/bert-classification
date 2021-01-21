from datasets.base_label_mapper import BaseMapperBase


class SST2LabelMapper(BaseMapperBase):
    """
    Maps string labels to integers for sst2 dataset
    """

    def __init__(self):
        self._raw_labels = ["0", "1"]

        self._map = {v: i for i, v in enumerate(self._raw_labels)}

        self._reverse_map = {i: v for i, v in enumerate(self._raw_labels)}

    def map(self, item) -> int:
        return self._map[item]

    def reverse_map(self, item: int):
        return self._reverse_map[item]

    @property
    def num_classes(self) -> int:
        return len(self._reverse_map)

    @property
    def positive_label(self):
        return self.reverse_map(self.positive_label_index)

    @property
    def positive_label_index(self) -> int:
        return self.map("Positive")
