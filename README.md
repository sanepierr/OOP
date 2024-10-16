CarRental-

Vehicle Class

Write a class Vehicle. A Vehicle has an instance variable to store the color of the Vehicle. The color can be retrieved with the getColor() method. The toString() method returns a String like This vehicle is red, depending on the actual color.

Car Class

Write a class Car that extends the class Vehicle. A car has an instance variable of type boolean to define whether it has winter tires or not (default value: false). The method toString() of the class Car prints the same message as the method of the class Vehicle, but it does also add another line with the content: has winter tires: true/false, depending on the actual value.

Truck Class

Write a class Truck that extends the class Vehicle. A truck has an instance variable of type boolean to define whether it has a trailer or not (default value: false). The method toString() of the class Truck prints the same message as the method of the class Vehicle, but it does also add another line with the content: has trailer: true/false, depending on the actual value.

Garage Class

Write a class Garage that has a Vehicle as an instance variable. This garage can be used by Cars and Trucks. Define a method setVehicle(Vehicle parked) to park a vehicle in the garage. Provide a method toString() to print a message Description of the parked vehicle ... followed by the description of the vehicle that is in the garage at this moment.

GarageTester Class

Write a class GarageTester with a method getExample() (see template). In this method, create an object of the Truck class (color is black, and the truck has no trailer). Create an object of the Garage class. Put the Truck into the Garage.

Customer Class

Write a class Customer that contains a name and an address of a customer.