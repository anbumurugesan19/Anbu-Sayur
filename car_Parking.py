# parkingLot list 
parkingLot = [["1", "0", "1"],["0", "1", "0"]]

# Already parked carIds key as carID, value as position [rows, cols]
carIds = {"111": [0, 0],
          "112": [0, 2],
          "113": [1, 1]}

# This function is used to start the parkingSpace as fully empty
# def initParking(rows, cols):

#     for row in range(rows):
#         parkingLot.append([])
#         for col in range(cols):
#             parkingLot[row].append("0")


# This function is used for Allocate a space for coming cars.....
def allocateSpace(carId):

    for rows in range(len(parkingLot)):
        for cols in range(len(parkingLot[rows])):
            if parkingLot[rows][cols] == "0":
                parkingLot[rows][cols] = "1"
                # Add the carId and particular car position(rows, cols) to the CardIds dictionary
                carIds.update({carId : [rows, cols]})
                return f"Allocated space for carId {carId} is {rows}{cols}"
    
    return f"Sry CarId {carId}. Space is full, Find a another spot for car Parking"

#This function is used for leave the parking cars
def leavingCars(lcarId):
    for i in lcarId:
        row = carIds[i][0]
        col = carIds[i][1]
        parkingLot[row][col] = 0
        print(f"This CarId {i} is leaving at the position of {row}{col}")



print(f"Inital parkingLot: {parkingLot}\n")
# initParking(rows, cols)
comingCars = int(input("Enter the no of Coming Cars: "))

#This for is used
for i in range(0, comingCars):
    print(allocateSpace("10" + str(i)))
print(f"\nParkingLot after allocating a space: {parkingLot}")

#Print the CarIds dictionary 
print(f"CarIds: {carIds}")

# leaving cars carId list
leavingCarsCarId = input("\nLeaving CarId: ").split(" ") #"112","100"
leavingCars(leavingCarsCarId)


print(f"Final ParkingLot: {parkingLot}")


