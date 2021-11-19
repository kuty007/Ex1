# Ex1     
![Add a heading](https://user-images.githubusercontent.com/93159965/142401078-a0e123fc-2079-425a-9c84-d065401279c1.png)
                           
# ID: 206316895,318786506
## Description:

When we come to analyze the problem of the optimal way to use an elevator in a building- we encounter a number of  problems, for example:
  Are all the calls known to us in advance or do we receive a live stream of calls (offline VS online)?
 
  
How to allocate our elevators the best? Should each elevator be limited with specific  range of floors that it handles or can each elevator respond to calls from all floors?

Which call to handle first - the call that came first? Or the call that we can handle the fastest? This question can lead to a "starvation" of distant floors.
Will the same strategy work effectively in a 10 floors and 100 floors building or is there a fundamental difference between them?

## Articles:

We have come across a number of articles that have lightened our eyes in every form of approach to the problem and its importance to other areas of our lives.

![Add a heading (2)](https://user-images.githubusercontent.com/93159965/142402726-aff88a2a-b157-4b99-97b2-f37270e0a468.png)

Article number 1. is actually an article that presents the complexity of the possible way of thinking and looking at the importance of time algorithms, and the differences between them.
There are two more- SCAN and LOOK algorithms.
The algorithms work similarly but LOOK is slightly better. SCAN goes in one direction and handles all the calls that are in that direction until it reaches the end and then goes back to the other side and handles all the calls in the other direction. LOOK is more efficient, if he has no more calls in the direction he is going then he changes direction and handles the calls in the other direction.

Article number 2. deals with the algorithm in a rather simplistic way and deals more with general questions around as we mentioned in the introduction above. Also in the article it is noted that today many buildings use artificial intelligence to determine the best way to operate the elevators.
 The video (source number 4) shows this out and presents a problem similar to what there is in the task- of having different types of buildings and elevators.
 
Article number 3. is actually a comparison between the five known elevator algorithms before the 2000’s:
- MRF-Maimum  Request First
- FRF- First Request First
- RAND-Random
- CIRC -Cicular
- SDF - Shortesst Destination First

The comparison between these five helps to understand the importance of logic and planning before approaching the realization of projects of this magnitude.

## Bibliography:


# 1.https://cdmana.com/2021/02/20210202111024127g.html

# 2.https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/

# 3.https://nanopdf.com/download/comparative-study-of-on-line-algorithms-for-the-elevator-scheduling_pdf

# 4.https://www.bjmc.lu.lv/fileadmin/user_upload/lu_portal/projekti/bjmc/Contents/8_4_12_Robal.pdf 

- A short video that clearly illustrates the problem:
# https://www.youtube.com/watch?v=xOayymoIl8U
  
## Offline Algorithm:
 
- 1.1) get building and a call 
- 1.2) create a variable that will eventually will be the id of the allocated elevator for this call and call it chosen_elv 

- 1.3)  create a variable that hold max int value and call it min_time
- 2) call for delete_busy function to clear done calls time
- 3)  assign into variable free_elv  the value from unbusy_elv function
- 3.1) if  free_elv !=-1:
		allocate  free_elv to this call
		add to call for the free_elvr call list
		add the finish time for this call to free_elv  busy_time list 
- 4) else iif  free_elv == -1:
- 4.1)loop on all elevators on the building
- 4.2) create a variable temp
temp = the difference between the last call the elevator handling to the time of the new call+ the time that will take to this elevator to complete this call
- 4.3) if temp< min_time:
		min_time =temp
		chosen_elv = building.elevators[i]
		

- 5)after we finish the loop 
- 5.1)allocate chosen_elv to this call
add to call for the chosen_elvcall list
add the finish time for this call to chosen_elv  busy_time list 

 #done!#

## functions explanations:
- unbusy_elv:
--->loop all over the elevators on the building
--->if elevator don't have any calls that she work on chack the time to complete this call
--->get the unbusy elevator  with the best time and return it index

- time_for_call:
this function calculate the time that will take to complete Elevator call
by take all the stops the elevator need to to do and the distance she need to travel 
and take consider of the elevator attributes
- delete_busy:
check if the new call time is bigger from the values of busy time for each elevator and if so delete them

## UML

![image](https://user-images.githubusercontent.com/93159965/142508974-04daff6d-df55-47a3-a2b2-6d342c1b7721.png)





