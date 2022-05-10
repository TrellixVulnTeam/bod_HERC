
from srcap.uitls.manager import Manager

manager = None


def init_():
    global manager
    manager = Manager(threaded=True, no_resize=False)


def get_the_manager():
    return manager


init_()
