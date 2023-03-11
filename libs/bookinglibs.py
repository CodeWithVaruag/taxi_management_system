class Booking():
    def __init__(self,bid=0,initial_address=None,final_address=None,pickup_date=None,pickup_time=None,bookings_status=None,cid=None,did=None):
        self.bid=bid
        self.initial_address=initial_address
        self.final_address=final_address
        self.pickup_date=pickup_date
        self.pickup_time=pickup_time
        self.booking_status=bookings_status
        self.cid=cid
        self.did=did


    def getBid(self):
        return self.bid

    def getInitial_address(self):
        return self.initial_address

    def getFinal_address(self):
        return self.final_address

    def getPickup_date(self):
        return self.pickup_date

    def getPickup_time(self):
        return self.pickup_time

    def getBooking_status(self):
        return self.booking_status

    def getCid(self):
        return self.cid

    def getDid(self):
        return self.did





    def setBid(self,bid):
        self.bid=bid

    def setInitial_address(self,initial_address):
        self.initial_address=initial_address

    def setFinal_address(self,final_address):
        self.final_address=final_address

    def setPickup_date(self,pickup_date):
        self.pickup_date=pickup_date

    def setPickup_time(self,pickup_time):
        self.pickup_time=pickup_time

    def setBooking_status(self,booking_status):
        self.booking_status=booking_status

    def setCid(self,cid):
        self.cid=cid

    def setDid(self,did):
        self.did=did



    def __str__(self):
        return str("{}, {}, {}, {}, {}, {}".format(self.bid,self.initial_address,self.final_address,
        self.pickup_date,self.pickup_time,self.booking_status,self.cid,self.did))



