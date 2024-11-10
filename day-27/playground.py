#unlimited arguments
def add(*nums):
    sum = 0
    print(nums[0])
    for n in nums:
        sum += n
    return sum

#unlimited_keywords
def calculate(n, **unlimited_keywords):
    # print(unlimited_keywords)
    # print(type(unlimited_keywords))
    m = 1
    l = 1
    m += unlimited_keywords["add"]
    l *= unlimited_keywords["multiply"]

    print(m)
    print(l)



# print(add(2,3))
# print(add(2,3,4))
calculate(3, add=2, multiply=3)

class Car:
    def __init__(self, **possibly_car_attributes):
        self.brand = possibly_car_attributes["brand"]
        self.name = possibly_car_attributes.get("name")
        self.color = possibly_car_attributes["color"]

car = Car(brand="SAN", name="Fan", color="red")
print(car.brand)
print(car.name)
print(car.color)