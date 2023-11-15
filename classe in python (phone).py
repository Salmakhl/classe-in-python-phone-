class phone():
    def __init__(self,brand,name,ram,color) :
        self.brand=brand
        self.name=name
        self.ram = ram
        self.color = color
        
       

    def information(self):
        print("the brand is :{} ,name {} , RAM {} and color {}. "
              .format(self.brand,self.name,self.ram,self.color))


#the main programe
p1=phone("Sumsang","The Galaxy S23 Ultra",16,"black")
p2=phone("asus", "The ROG Phone 6", 18,"red")
p3=phone("one plus","oneplus 11",18,"pink")



p1.information()
p2.information()
p3.information()




 