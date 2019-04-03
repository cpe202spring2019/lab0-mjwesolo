def weight_on_planets():
    weight = input("What do you weigh on earth? ")
    
    mars = int(weight) * 0.38
    jupiter = int(weight) * 2.34
    
    print("\nOn Mars you would weigh", mars, "pounds.")
    print("On Jupiter you would weigh", jupiter, "pounds.")
   
   
   
if __name__ == '__main__':
   weight_on_planets()
