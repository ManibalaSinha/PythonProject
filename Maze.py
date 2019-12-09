from enum import Enum

class MapSite():
    def Enter(self):
        raise NotImplementedError('Abstract Base Class method')

class Direction(Enum): #1. creating name of direction with using enum
    North = 0
    East  = 1
    South = 2
    West  = 3
    
class Room(MapSite): #2.created the Room class that inherit from MapSite
    def __init__(self, roomNo):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)

    def GetSide(self, Direction):
        return self._sides[Direction]

    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite

    def Enter(self): #inherit and overwrite Enter()method
        print('You have entered room: ' + str(self._roomNumber))

class Wall(MapSite): #2 create some classes that inherit from MapSite
    def Enter(self): #inherit and overwrite Enter()method
        print(' * You just ran into a Wall...')

class Door(MapSite): #2.created the Door class that inherit from MapSite
    def __init__(self, Room1=None, Room2=None): #Door knows the room, we pass Room1, Room2
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False
        
    def OtherSideFrom(self, Room): #which room is other side side of door
        print('\tDoor obj : This door is side of room: {}'.format(Room._roomNumber))
        if 1 == Room._roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1
        return other_room

    def Enter(self): #inherit and overwrite Enter()method
        if self._isOpen: print('You have passed through this door.....')
        else: print(' ** This door needs to be opened before you can pass through it...')

class Maze():
    def __init__(self):
        # dictionary to hold room_number, room_obj <key, value> pairs
        self._rooms = {}

    def AddRoom(self, room):
        #use roomNumber as lookup value to retrieve room object
        self._rooms[room._roomNumber] = room

    def RoomNo(self, room_number):
        return self._rooms[room_number] 

class MazeGame():
    def CreateMaze(self):
        aMaze = Maze() # create Maze by initiating aMaze
        r1 = Room(1)# initiating room by giving room number 1
        r2 = Room(2) #initiating other room
        theDoor = Door(r1, r2)# room on the each side of door
        
        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)
        # 4 side of the 2 room
        r1.SetSide(Direction.North.value, Wall())
        r1.SetSide(Direction.East.value, theDoor) 
        r1.SetSide(Direction.South.value, Wall())  
        r1.SetSide(Direction.West.value, Wall())  
        
        r2.SetSide(Direction(0).value, Wall())
        r2.SetSide(Direction(1).value, Wall()) 
        r2.SetSide(Direction(2).value, Wall()) 
        r2.SetSide(Direction(3).value, theDoor)    
        
        return aMaze
#-------------------# Self Testing Section #-------------------
if __name__ == '__main__':
 #   map_site_inst = MapSite() #instance of the abstract class
 #   map_site_inst.Enter() #call the enter() method on instance
    
    print('*' * 21)
    print( '*** The Maze Game ***')
    print('*' * 21)
    
    #create the Maze
    maze_obj = MazeGame().CreateMaze()#instance of the MazeGame() and create the CreateMaze() method on it
    
    #find its rooms
    maze_rooms = []#list of rooms
    for room_number in range(5): #trying to figure out, that our maze consists of 5 rooms
        try:
            #get the room number
            room = maze_obj.RoomNo(room_number)#calling RoomNo() method
            print('\n ^^^ Maze has room: {}'.format(room_number, room))
            print('   Entering the room...')
            room.Enter()
            #append rooms to list
            maze_rooms.append(room)
            for idx in range(4): #existing room having 4 sides
                side = room.GetSide(idx)
                side_str = str(side.__class__).replace("<class ' __main__.", "").replace("'>", "")
                print(' Room: {}, {:<15s}, Type: {}'.format(room_number, Direction(idx), side_str))
                print(' Trying to enter: ', Direction(idx))
                side.Enter()# Enter the side
                if 'Door' in side_str:
                    door = side
                    if  not door._isOpen:
                        print(' *** Opening the door...')
                        door._isOpen = True #if dooor is open
                        door.Enter() #we enter it
                    print('\t', door)
                    #find the which room on the other side of the door
                    other_room = door.OtherSideFrom(room)
                    print('\tOn the other side of the door is Room: {}\n'.format(other_room._roomNumber))

        except KeyError: #exception no room number
            print('No room:', room_number)
    num_of_rooms = len(maze_rooms)
    print('\n There are {} rooms in the Maze.'.format(num_of_rooms))

    print('Both doors are the same object and they are on the East and West side of the two rooms. ')
                        