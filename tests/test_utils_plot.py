"""
Trading-Technical-Indicators (tti) python library

File name: test_utils_plot.py
    tti.utils package, plot.py module unit tests.
"""

import unittest
import pandas as pd

from tti.utils import plot


class TestLinesGraph(unittest.TestCase):

    def test_data_parameter_missing(self):

        with self.assertRaises(TypeError):
            plot.linesGraph(y_label='Y', title='T', lines_color=['r'],
                            alpha_values=[0.5], areas=None, x_label='X')

    def test_y_label_parameter_missing(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        with self.assertRaises(TypeError):
            plot.linesGraph(data=df, title='T', lines_color=['r'],
                            alpha_values=[0.5], areas=None, x_label='X')

    def test_title_parameter_missing(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        with self.assertRaises(TypeError):
            plot.linesGraph(data=df, y_label='Y', lines_color=['r'],
                            alpha_values=[0.5], areas=None, x_label='X')

    def test_lines_color_parameter_missing(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        with self.assertRaises(TypeError):
            plot.linesGraph(data=df, y_label='Y', title='T',
                            alpha_values=[0.5], areas=None, x_label='X')

    def test_alpha_values_parameter_missing(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        with self.assertRaises(TypeError):
            plot.linesGraph(data=df, y_label='Y', title='T', lines_color=['r'],
                            areas=None, x_label='X')

    def test_areas_parameter_missing(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        with self.assertRaises(TypeError):
            plot.linesGraph(data=df, y_label='Y', title='T', lines_color=['r'],
                            alpha_values=[0.5], x_label='X')

    def test_x_label_parameter_missing(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        self.assertIsNotNone(plot.linesGraph(data=df, y_label='Y', title='T',
                                             lines_color=['r'],
                                             alpha_values=[0.5], areas=None))

    def test_data_parameter_wrong_type(self):

        with self.assertRaises(TypeError):
            plot.linesGraph(data=1, y_label='Y', title='T', lines_color=['r'],
                            alpha_values=[0.5], areas=None, x_label='X')

    def test_data_parameter_index_wrong_type(self):
        df = pd.DataFrame(index=range(3), columns=['A1'], data=[1, 2, 3])

        with self.assertRaises(TypeError):
            plot.linesGraph(data=df, y_label='Y', title='T', lines_color=['r'],
                            alpha_values=[0.5], areas=None, x_label='X')

    def test_data_parameter_two_dataframes(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        self.assertIsNotNone(plot.linesGraph(data=[df, df], y_label='Y',
                                             title='T', lines_color=['r', 'g'],
                                             alpha_values=[0.5, 0.5],
                                             areas=None, x_label='X'))

    def test_data_parameter_three_dataframes(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1', 'A2'],
                          data=[[1, 1], [2, 2], [3, 3]])

        self.assertIsNotNone(plot.linesGraph(data=[df, df, df], y_label='Y',
                                             title='T',
                                             lines_color=['r', 'g', 'b'],
                                             alpha_values=[0.5, 0.5, 0.5],
                                             areas=None, x_label='X'))

    def test_input_parameter_title(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        self.assertEqual(plot.linesGraph(data=df, y_label='Y', title='T',
                                         lines_color=['r'],
                                         alpha_values=[0.5], areas=None,
                                         x_label='X').gca().
                         get_title(), 'T')

    def test_input_parameter_x_label(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        self.assertEqual(plot.linesGraph(data=df, y_label='Y', title='T',
                                         lines_color=['r'],
                                         alpha_values=[0.5], areas=None,
                                         x_label='X').gca().get_xlabel(), 'X')

    # y_label is not tested because is defined with text function

    def test_input_parameter_lines_color(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        self.assertIsNotNone(plot.linesGraph(data=df, y_label='Y', title='T',
                                             lines_color=['red'],
                                             alpha_values=[0.5], areas=None,
                                             x_label='X'))

    def test_input_parameter_alpha_values(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1'], data=[1, 2, 3])

        self.assertIsNotNone(plot.linesGraph(data=df, y_label='Y', title='T',
                                             lines_color=['red'],
                                             alpha_values=[0.5], areas=None,
                                             x_label='X'))

    def test_input_parameter_areas(self):
        df = pd.DataFrame(index=pd.DatetimeIndex(['2018-01-01', '2018-01-02',
                                                  '2018-01-03']),
                          columns=['A1', 'A2'], data=[[1, 1], [2, 2],
                                                      [3, 3]])

        self.assertIsNotNone(plot.linesGraph(data=[df, df], y_label='Y',
                                             title='T',
                                             lines_color=['red', 'green',
                                                          'blue', 'black'],
                                             alpha_values=[0.5, 0.5, 0.5, 0.5],
                                             areas=[{'x': ['2018-01-01',
                                                           '2018-01-02'],
                                                     'y1': [1., 1.],
                                                     'y2': [3., 3.],
                                                     'color': 'red'}],
                                             x_label='X'))


if __name__ == '__main__':
    unittest.main()
