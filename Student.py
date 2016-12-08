class student:
    def __init__(self,name,hometown,age,height,ice_cream):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.ice_cream=ice_cream
    def print_summary(self):
        print(self.name+" "+self.hometown+" "+self.age+" "+self.height+" "+self.ice_cream)
