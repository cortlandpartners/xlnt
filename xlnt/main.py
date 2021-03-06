import xlwings as xw


class Enumeration:
    shift_to_right = -4161
    shift_down = -4121
    paste_all = -4104
    paste_formulas = -4123
    paste_formats = -4122
    paste_validation = 6


class App(xw.App):

    def __init__(self, visible=None, spec=None, add_book=True, impl=None):
        super().__init__(visible=visible, spec=spec, add_book=add_book, impl=impl)

    def enable_iterative_calculations(self, value=True, max_iterations=100, max_change=.001):
        self.api.iteration = value
        self.api.MaxIterations = max_iterations
        self.api.MaxChange = max_change

    @staticmethod
    def enable_events(self, value=True):
        # TODO: Build enable events
        pass


class Book(xw.Book):

    def __init__(self, file_path=None, update_links=False, read_only=True):

        self._app = None

        if xw.apps.count >= 1:
            self._app = xw.apps[0]
        elif file_path:
            self._app = xw.App(add_book=False)

        if file_path and not self.is_open(wb_path=file_path):
            self._app.books.api.Open(file_path, UpdateLinks=update_links, ReadOnly=read_only)

        super().__init__(fullname=file_path)

    def close(self, save_changes=False):

        if save_changes:
            self.save()

        if self.app.books.count == 1:
            self.app.quit()
        else:
            super().close()

    @staticmethod
    def is_open(wb_path):

        for app in xw.apps:
            for wb in app.books:
                if wb.fullname.lower() == wb_path.lower():
                    return True

        return False


class Sheet(xw.Sheet):

    def __init__(self, name):
        super().__init__(sheet=name)

    def range(self, cell1, cell2=None):
        try:
            super().range(cell1=cell1, cell2=cell2)
        except ValueError:
            return None

    def copy(self, before_index=None, after_index=None):

        # default to end if not index specified
        if not before_index and not after_index:
            after_index = self.book.sheets.count - 1

        if before_index:
            self.api.Copy(Before=self.book.sheets[before_index - 1].api)
            return self.book.sheets[before_index - 1]

        elif after_index:
            self.api.Copy(After=self.book.sheets[after_index + 1].api)
            return self.book.sheets[after_index + 1]
