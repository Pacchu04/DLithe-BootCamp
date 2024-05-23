# Keyword argument 

def person(name, ** data):
    print(name)

    for i,j in data.items():
        print(i,j)


def car(model,*features, **info):
    print("Car Model: ",model)
    for f in features:
        print(f" Features of SUV: {f}\n")
    
    for i,j in info.items():
        print(f" {i}: {j}")

d={'airbag':True,"seats":4}
#person('Jhon',age=28,city="Bangalore",mob=93283892)
car("SUV","Interior","Cargo Space","Durable Build Quality",d)