from model.List import List

class Node :

    def __init__(self, label : str, title : str, callback : str) :
        self.label : str = label
        self.title : str = title
        self.callback : str = title
        self.children = List()

class ActionTree :

    def __init__(self) :
        self.root = None
