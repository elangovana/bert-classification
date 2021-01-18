import csv
import logging
from collections import Counter

from torch.utils.data import Dataset


class SST2Dataset(Dataset):
    """
    The sst2 dataset
    """

    @property
    def logger(self):
        return logging.getLogger(__name__)

    def __init__(self, input_file, preprocessor=None, label_mapper=None):
        self.preprocessor = preprocessor
        self._items, self._labels = self._read_csv(input_file)
        self._label_mapper = label_mapper

    @property
    def _logger(self):
        return logging.getLogger(__name__)

    def _read_csv(self, input_file):
        self._logger.info("loading {}".format(input_file))
        data, labels = [], []

        with open(input_file, "r") as f:
            csv_reader = csv.reader(f, delimiter='\t',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for r in csv_reader:
                label = None
                text = r[0]

                # Has labels labels
                if len(r) == 2:
                    label = r[1]

                labels.append(label)
                data.append(text)

        self._logger.info("Loaded file {} with {} records ".format(input_file, len(data), Counter(labels)))
        return data, labels

    def __len__(self):
        return len(self._items)

    def __getitem__(self, idx):
        x, y = self._items[idx], self._labels[idx]

        if self.preprocessor:
            x = self.preprocessor(x)

        if self._label_mapper:
            y = self._label_mapper.map(y)

        return x, y
