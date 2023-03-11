class Customer():
    def __init__(self,cid=0,name=None,email=None,contact=None,address=None,password=None,payment=None):
        self.cid=cid
        self.name=name
        self.email=email
        self.contact=contact
        self.address=address
        self.password=password
        self.payment=payment

    def getCid(self):
        return self.cid

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

    def getPayment(self):
        return self.payment



    def setCid(self,cid):
        self.cid=cid

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
        return str("{}, {}, {}, {}, {}, {}".format(self.cid,self.name,self.email,self.contact,self.address,self.password,self.payment))


