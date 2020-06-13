#parent class
class Predator:
    
    def __init__(self):
        print("Lion is ready")
        
    def who_is_this(self):
        print("Lion")
        
    def run(self):
        print("run faster")

#child class
class Lion:
    
    def __init__(self):
        
        #call super() function
        super().__init__()
        print("Lion is ready")
    
    def who_is_this(self):
        print("Lion")
        
    def run(self):
        print("Run Faster")
        
leo = Lion()
leo.who_is_this()
leo.run()