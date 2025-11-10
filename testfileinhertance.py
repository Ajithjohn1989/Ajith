class Football_Clubs:
    count=0
    def details(self,name,jcolor,owner,sponser,orgin):

        self.jcolor=jcolor
        self.name=name
        self.owner=owner
        self.sponser=sponser
        self.orgin=orgin

class Teams(Football_Clubs):
    def __init__(self,name,stadium,capacity,parking):
        self.name=name
        self.stadium=stadium
        self.capacity=capacity
        self.parking=parking

    def display_details(self):
        print("Name: ",self.name)
        print("Owner : ",self.owner)
        print("Sponsor : ",self.sponser+" "+self.orgin)
        print("Parking : ",self.parking)

Team1=Teams("AC Milan","San Siro",20000 ,"30000")

Team1.details("AC Milan","Red&Black","RedBird Capital Partners","RedBull Racing","Italy")
Team1.display_details()