from unittest import TestCase
from ProgressBar import ProgressBar


class TestProgressBar(TestCase):

    def test_set_value(self):
        """
        Test if the set_value method works
        """

        pb = ProgressBar()
        pb.set_value(87.8674)

        self.assertEqual(pb.get_value(), 87.8674)

    def test_progress_1_argument(self):
        """
        Test if progress method with 1 argument return the good percentage

        For this case, we can try to imagine one loop statement that runs through 2 values:
            -> 100/2 = 50
        """

        pb = ProgressBar()
        pb.progress(2)

        self.assertEqual(pb.get_value(), 50)

    def test_progress_2_arguments(self):
        """
        Test if progress method with 2 arguments return the good percentage
        """

        pb = ProgressBar()
        pb.progress(4, 5)

        self.assertEqual(pb.get_value(), 5)

    def test_progress_3_arguments(self):
        """
        Test if progress method with 2 arguments return the good percentage
        """

        pb = ProgressBar()
        pb.progress(5, 2, 8)

        self.assertEqual(pb.get_value(), 1.25)


if __name__ == '__main__':
    TestProgressBar.main()
