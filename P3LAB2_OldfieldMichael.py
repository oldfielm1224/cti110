userservice = (input('Enter desired auto service:\n'))

print ('You entered:', userservice)

if userservice == 'Oil change':
    print ('Cost of oil change: $35')
    
elif userservice == 'Tire rotation':
    print ('Cost of tire rotation: $19')
        
elif userservice == 'Car wash':
    print ('Cost of car wash: $7')
            
else:
    print ('Error: Requested service is not recognized')
                