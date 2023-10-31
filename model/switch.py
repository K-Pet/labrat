import meta


class Switch(meta.Meta):
    def __init__(self, id, name) -> None:
        super().__init__(id, name)
        self.NumPorts = 0
        self.PortSpeed = 0
        self.Model = None
        self.Vendor = None
        self.SerialNumber = None
        self.ManagementIP = None