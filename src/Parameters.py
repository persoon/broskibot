

class Parameters:
    """
       Borg pattern --- https://stackoverflow.com/questions/747793/python-borg-pattern-problem/747888#747888
       """
    __we_are_one = {}

    client = None

    def __init__(self):
        self.__dict__ = self.__we_are_one