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

class Data_entertainments:
    def __init__(self, name, address, number_phone, website = None):
        self.name = name
        self.address = address
        self.number_phone = number_phone
        self.website = website
class Data_eat:
    def __init__(self, name, address, number_phone, website = None):
        self.name = name
        self.address = address
        self.number_phone = number_phone
        self.website = website

class Data_studu:
    def __init__(self, name, description, website = None):
        self.name = name
        self.description = description
        self.website = website

class Data_school:
    def __init__(self, name, website = None):
        self.name = name
        self.website = website