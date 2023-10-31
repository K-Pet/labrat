import meta


class Datacenter(meta.Meta):
    def __init__(self, id, name, address) -> None:
        super(meta.Meta, self).__init__(id, name)
        self.Address = address
        self.LabIDs = set() # set of lab IDs
