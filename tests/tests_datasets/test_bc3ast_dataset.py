import os
from unittest import TestCase

from datasets.sst2_dataset import SST2Dataset


class TestBC3ASTDataset(TestCase):

    def test___getitem__(self):
        file = os.path.join(os.path.dirname(__file__), "..", "sample_sst2.csv")
        sut = SST2Dataset(file)
        expected_y = "Positive"
        expected_x = "But he somehow pulls it off ."

        # Act
        actual_x, actual_y = sut.__getitem__(7)

        # Assert
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_x, actual_x)
