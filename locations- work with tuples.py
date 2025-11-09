location = []
for x in range (3):
    a = str(input("Enter the name of the location: "))
    n = float(input("Enter the length of the location: "))
    k = float(input("Enter the latitude of the location: "))
    ## this is the tuple definition
    place = (a,n,k)
    location.append(place)

print(location)
