class Admin():
    def __init__(self,aid=0,name=None,email=None,contact=None,address=None,password=None):
        self.aid=aid
        self.name=name
        self.email=email
        self.contact=contact
        self.address=address
        self.password=password


    def getAid(self):
        return self.aid

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getContact(self):
        return self.contact

    def getAddress(self):
        return self.address

    def getPassword(self):
        return self.password



    def setAid(self,aid):
        self.aid=aid

    def setName(self,name):
        self.name=name

    def setEmail(self,email):
        self.email=email

    def setContact(self,contact):
        self.contact=contact

    def setAddress(self,address):
        self.address=address

    def setPassword(self, password):
        self.password = password

    def setPayment(self,payment):
        self.payment = payment


    def __str__(self):
        return str("{}, {}, {}, {}, {}, {}".format(self.aid,self.name,self.email,self.contact,self.address,self.password))


