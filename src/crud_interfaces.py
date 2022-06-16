from abc import ABC, abstractmethod

# These interfaces apply the Interface Segregation Principle (ISP)
# Each CRUD functionality is separated into each interface and only used if needed

class CreateObjectInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_one(object):
        pass

    @staticmethod
    @abstractmethod
    def create_many(objects):
        pass

class ReadObjectInterface(ABC):
    @staticmethod
    @abstractmethod
    def read_one(id):
        pass

    @staticmethod
    @abstractmethod
    def read_many(ids):
        pass

    @staticmethod
    @abstractmethod
    def is_empty():
        pass

class UpdateObjectInterface(ABC):
    @staticmethod
    @abstractmethod
    def update_one(id, object):
        pass

class DeleteObjectInterface(ABC):
    @staticmethod
    @abstractmethod
    def delete_one(id):
        pass

    @staticmethod
    @abstractmethod
    def delete_many(id):
        pass
