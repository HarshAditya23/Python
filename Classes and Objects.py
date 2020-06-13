class Lion:
    
    #class attributes
    species = "bird"
    
    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)

#instantiate the Lion class        
rummy = Lion("Rummy", 16)
tison = Lion("Tison", 23)


#access the class attributes
print("Rummy is a {}".format(rummy.__class__.species))
print("Tison is also a {}".format(tison.__class__.species))

#access the instance attributes
print("{} is {} years old".format(rummy.name, rummy.age))
print("{} is {} years old".format(tison.name, tison.age))

#calling our instance methods
print(tison.sing("Happy"))
print(rummy.dance())