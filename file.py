import os
import tempfile

class File:

    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(filename) is False:
            f = open(filename, 'w')
            f.write('')
            f.close()

    def __str__(self):
        return self.filename

    def __add__(self, other):
        f1 = open(self.filename, 'r')
        str1 = f1.read()
        f1.close()
        f2 = open(other.filename, 'r')
        str2 = f2.read()
        f2.close()
        new_f = File(os.path.join(tempfile.gettempdir(), 'newfile'))
        new_f.write(str1 + str2)
        return new_f




    def __iter__(self):
        self.f = open(self.filename, 'r')
        return self

    def __next__(self):
        result = self.f.readline()
        if not result:
            self.f.close()
            raise StopIteration
        return result


    def read(self):
        f = open(self.filename, 'r')
        str = f.read()
        f.close()
        return str

    def write(self, str):
        f = open(self.filename, 'w')
        f.seek(0)
        f.write(str)
        f.close()

