import os
import string

class ErrorReadingFile(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super(Exception, self).__init__(message)


class ParseFile(object):

    def __init__(self, file_path, base_folder= None):
        if base_folder is None:
            base_folder = os.path.dirname(os.path.realpath(__file__)) + '/'
        self.file_path = base_folder+file_path
        self.data = dict()

    def parse(self, separator=';'):
        fd = open(self.file_path, 'rb')  #open the file
        rows = fd.readlines()
        if len(rows) is 0:
            raise ErrorReadingFile('noline in file')


        values=rows[0].split(separator)
        n_columns = len(values)

        print 'file contains ', len(rows), 'lines and ', n_columns, 'columns'

        for i in range(0,n_columns):
            self.data[i] = list()

        for r in rows:
            spl_line = r.split(separator)

            if len(spl_line) != n_columns:
                fd.close()
                raise ErrorReadingFile('unexpected number of column in a row')

            curr_col = 0
            for col in spl_line:
                if ',' in col:
                    col = string.replace(col, ',', '.')
                self.data[curr_col].append(float(col))
                curr_col += 1
        fd.close()

        return self.data
