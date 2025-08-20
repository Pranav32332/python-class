class Employee : 
    def accept (self): 
        self.name=str(input("enter a name of empolyee")) 
        self.id=str(input("enter the id  of  empolyee")) 
        self.salary=int(input("enter the number of empolyee"))   
        self.location=str(input ("enter the location  of empolyee"))  
        self.department=str(input("enter the department  of empolyee"))     
    
    def show (self): 
          print("name of empolyee ",self.name) 
          print("id of empolyee", self.id)  
          print("salary of empolyee",self.salary) 
          print("location of empolyee",self.location) 
          print(" department of empolyee",self.department)     

emp=Employee()
emp.accept() 
emp.show()
