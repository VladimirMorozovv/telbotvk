class Data_user:
    def __init__(self, telegchatID, username, name):
        self.telegchatID = telegchatID
        self.username = username
        self.name = name


class Data_medical:
    def __init__(self, name, address, number_phone, website = None):
        self.name = name
        self.address = address
        self.number_phone = number_phone
        self.website = website