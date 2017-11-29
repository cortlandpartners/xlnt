import os
import xlnt as xl

dir_path = os.path.dirname(os.path.realpath(__file__))
wb_path = os.path.join(dir_path, 'Test Workbook.xlsx')


def test_open():
    wb = xl.Book(file_path=wb_path)
    assert wb is not None
