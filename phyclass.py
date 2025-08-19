class Empolyee: 
    def  __init__(self,name,id,salary): 
        self.name=name 
        self.id =id 
        self.salary =salary 

    def display(self): 
     print("Empolyee information") 
     print("name :",self.name) 
     print("id : ",self.id) 
     print("salary: ", self.salary) 

e1=Empolyee("piyush",123,777) 
e2=Empolyee("pranav",555,6565) 
e3=Empolyee("karthik",545,7673) 
e2.display()
e1.display() 
e3.display()        