from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def writeData(self, data):
        pass

    @abstractmethod
    def readData(self) -> str:
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self._file = filename

    def writeData(self, data):
        with open(self._file, "a") as f:
            f.write(data)

    def readData(self) -> str:
        with open(self._file, "r") as f:
            return f.read()


class EncryptionDecorator(DataSource):
    def writeData(self, data):
        return ''.join([str(ord(c) for c in data)])

    def readData(self) -> str:
        data = ""
        return ''.join([str(chr(c) for c in data)])