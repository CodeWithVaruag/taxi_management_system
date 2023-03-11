class Diver():
    def __init__(self,did=0,name=None,email=None,contact=None,address=None,password=None,lisence_no=None,car_no=None,driver_status=None):
        self.did=did
        self.name=name
        self.email=email
        self.contact=contact
        self.address=address
        self.password=password
        self.car_no=car_no
        self.lisence_no=lisence_no
        self.driver_status=driver_status

    def getDid(self):
        return self.did

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getContact(self):
        return self.contact

    def getAddress(self):
        return self.address

    def getCar_no(self):
        return self.car_no

    def getLisence_no(self):
        return self.lisence_no

    def getPassword(self):
        return self.password

    def getDriver_status(self):
        return self.driver_status


    def setDid(self, did):
        self.did = did

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setContact(self, contact):
        self.contact = contact

    def setAddress(self, address):
        self.address = address

    def setCar_no(self, car_no):
        self.car_no = car_no

    def setLisence_no(self, lisence_no):
        self.lisence_no = lisence_no

    def setPassword(self, password):
        self.password = password

    def setDriver_status(self,driver_status):
        self.driver_status=driver_status



    def __str__(self):
        return str("{}, {}, {}, {}, {}, {}".format(self.did,self.name,self.email,self.contact,self.address,self.password,self.car_no,self.lisence_no,self.driver_status))


