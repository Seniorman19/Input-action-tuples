# An Adventure Game Template

def main():

    rooms = ((1,2,3),(0,),(0,),(0,4,6),(3,5),(4,),(3,7),(6,8),(7,9))
    roomnames=('Basement','Dusy Painting','Basement part 2','Kitchen',
               'Living Room','Secret Room','Dark Room','Garage','Driveway','Outside')
    items=['','1/11/16','','Crowbar','Motorbike Key','','Candle','','','']
    inventory=[]


    currentroom = 0
    nextroom = 0
    getroom = ''
    
    while (getroom != 'x'):

        print('Current room #{0}: {1}'.format(currentroom,roomnames[currentroom]))

        # If there is an item in this room, add it to the inventory
         # and remove it from the items list replacing it with ''

        if items[currentroom]!='':
            print("You found a {0}!".format(items[currentroom]))
            inventory.append(items[currentroom])
            items[currentroom]=''
        
        
        print('You can move to these rooms:')

        for i in rooms[currentroom]:
            print("\t Room #{0}: {1}".format(i,roomnames[i]))
            

        getroom = input('Where to? ')

        if getroom.isnumeric():
            nextroom=int(getroom)
            
        if nextroom in rooms[currentroom]:
            currentroom=nextroom

        print(inventory)
 
main()
