def cost_of_trip (return_flight,hostel_stay,car_rental,days=14,):
        cost = return_flight + (hostel_stay*days) + car_rental
        return cost

print('Cost of trip to Paris is $', cost_of_trip(200,20,200))
print('Cost of trip to London is $', cost_of_trip(250,30,120))
print('Cost of trip to Dubai is $', cost_of_trip(370,15,80))
print('Cost of trip to Mumbai is $', cost_of_trip(450,10,70))


