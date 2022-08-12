weight = 4.8
#Ground shipping
if  weight <= 2:
  cost_ground_shipping = weight *  1.50 + 20
elif weight <=6:
   cost_ground_shipping = weight * 3.00 + 20
elif weight <=10:
   cost_ground_shipping = weight * 4.00 + 20 
else:
   cost_ground_shipping = weight * 4.75 + 20  

print( cost_ground_shipping)
#Ground Shipping Premuim
cost_premuim_ground = 125
print(cost_premuim_ground)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <=6:
  cost_drone = weight * 9.00
elif weight <=10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25   
print( cost_drone)  

