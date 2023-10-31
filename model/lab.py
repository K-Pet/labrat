import meta


class Lab(meta.Meta):
    def __init__(self, id, name) -> None:
        super(meta.Meta, self).__init__(id, name)
        self.RackIDs = set() # set of rack IDs

class Rack(meta.Meta):
    def __init__(self, id, name) -> None:
        super().__init__(id, name)
        self.ServerIDs = dict()
        self.SwitcheIDs = dict()