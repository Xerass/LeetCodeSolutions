class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        #create a tuple array first
        
        #i love list comprehension
        cars = sorted([(p,s) for p,s in zip(position,speed)], reverse = True)

        print(cars)

        fleet_arrival = -(float('inf'))
        fleet_count = 0

        #now, we can push and pop them boys
        for car in cars:
            pos = car[0]
            speed = car[1]

            #main logic:

            #mathematically, this can be solved by creating a d v t graph and simply check where they intersect
            #intersecting lines are fleets.

            #but we can dumb it down, since our array is sorted by position, we know that every car cannot overtake the car in front
            #this means that a car is part of the fleet before it or not, so we only need to check once 
            #this also means that say if car has TOA of 4, and the car after it has a TOA of 2 (toa under assumption of no OTHER car on the street, much like the graph sol)
            #this allows us to see, IF TOA of car before is > TOA of car after, after car MUST become part of the fleet
            #with this intuition, we dont need to keep track of the cars themselves, but the last speed of the last fleet.
            #we then use this new fleet as the next "before" car and the following one as the after car
            time_of_arrival = (target - pos) / speed

            #to determine if we have another fleet, we simply need to check if time_of_arrival > fleet_arrival
            #since we only need to track number of car_fleets, we only ever need to check if fleet_arrival time changes
            if time_of_arrival > fleet_arrival:
                fleet_arrival = time_of_arrival
                fleet_count += 1 


        return fleet_count
