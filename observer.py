from abc import ABC, abstractmethod


class CameraSystem:
    """Централизованная система наблюдения."""

    def __init__(self):
        self.__observers = set()

    def attach(self, observer):
        self.__observers.add(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.make_photo()


class AbstractObserver(ABC):
    @abstractmethod
    def make_photo(self):
        pass


class Camera(AbstractObserver):
    """Камера наблюдения."""

    def __init__(self, name):
        self.name = name

    def make_photo(self):
        print('{} сделала фото'.format(self.name))


cam1 = Camera('Камера #1')
cam2 = Camera('Камера #2')
cam3 = Camera('Камера #3')
# Создадим центральный пульт управления.
cam_system = CameraSystem()
# Подключим все 3 камеры к пульту управления.
cam_system.attach(cam1)
cam_system.attach(cam2)
cam_system.attach(cam3)
cam_system.notify()
# >>> Камера #1 сделала фото
# >>> Камера #2 сделала фото
# >>> Камера #3 сделала фото
# Отключим первую камеру от пульта, т.к. фотки с нее получаются не четкие
cam_system.detach(cam1)
cam_system.notify()
