import os
from unittest import TestCase

from datasets.bc3ast_dataset import BC3ASTDataset


class TestBC3ASTDataset(TestCase):

    def test___getitem__(self):
        file = os.path.join(os.path.dirname(__file__), "..", "sample_bc3ast.csv")
        sut = BC3ASTDataset(file)
        expected_y = "0"
        expected_x = "Test line."

        # Act
        actual_x, actual_y = sut.__getitem__(4)

        # Assert
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_x, actual_x)
