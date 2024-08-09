class FileUtil:
    def read(self, path):
        b = None
        with open(path, 'rb') as f:
            b = f.read()
        return b

    def write(self, path, b):
        with open(path, 'ab') as f:
            f.write(b)
