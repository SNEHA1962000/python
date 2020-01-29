name=input("enter the name:")

def function(location,destination,facility):
    if facility=="ac":
       cost=5
       kms=250
       total=kms* cost
       print(total) 
    elif facility=="non_ac":
      cost=10
      kms=250
      total=kms* cost
      print(total)
    else:
        return 0;
location=input("enter the location:")
destination=input("enter the destination:")
facility=input("enter the facility:")
function(location,destination,facility)
print("name",name)
print("location",location)
print("destination",destination)
print("facility",facility)
print("**********************")
