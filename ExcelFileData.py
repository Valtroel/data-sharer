class ExcelFileData:
    def __init__(self, path, data):
        self.path = path
        self.data = data

    def __str__(self):
        return f'''
        ExcelFileData(
        path={self.path},
        data={self.data}
        )
        '''
