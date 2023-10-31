import meta


class Server(meta.Meta):
    def __init__(self, id, name) -> None:
        super(meta.Meta, self).__init__(id, name)
        self.SerialNumber = None
        self.BoardIP = None
        self.Model = None
        self.OS = None
        self.Cores = None
        self.Memory = None
        self.Storage = None