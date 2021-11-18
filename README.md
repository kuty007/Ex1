# Ex1                                    
# ID: 206316895,318786506
## Description:

When we come to analyze the problem of the optimal way to use an elevator in a building- we encounter a number of  problems, for example:
  Are all the calls known to us in advance or do we receive a live stream of calls (offline VS online)?
  
How to allocate our elevators the best? Should each elevator be limited with specific  range of floors that it handles or can each elevator respond to calls from all floors?

Which call to handle first - the call that came first? Or the call that we can handle the fastest? This question can lead to a "starvation" of distant floors.
Will the same strategy work effectively in a 10 floors and 100 floors building or is there a fundamental difference between them?

## Articles:

We have come across a number of articles that have lightened our eyes in every form of approach to the problem and its importance to other areas of our lives.

Article number 1. is actually an article that presents the complexity of the possible way of thinking and looking at the importance of time algorithms, and the differences between them.
There are two more- SCAN and LOOK algorithms.
The algorithms work similarly but LOOK is slightly better. SCAN goes in one direction and handles all the calls that are in that direction until it reaches the end and then goes back to the other side and handles all the calls in the other direction. LOOK is more efficient, if he has no more calls in the direction he is going then he changes direction and handles the calls in the other direction.

Article number 2. deals with the algorithm in a rather simplistic way and deals more with general questions around as we mentioned in the introduction above. Also in the article it is noted that today many buildings use artificial intelligence to determine the best way to operate the elevators.
 The video (source number 4) shows this out and presents a problem similar to what there is in the task- of having different types of buildings and elevators.
 
Article number 3. is actually a comparison between the five known elevator algorithms before the 2000’s:
a. MRF-Maimum  Request First
b. FRF- First Request First
c. RAND-Random
d. CIRC -Cicular
e. SDF - Shortesst Destination First

The comparison between these five helps to understand the importance of logic and planning before approaching the realization of projects of this magnitude.

## Bibliography:


1.https://cdmana.com/2021/02/20210202111024127g.html

2.https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/

3.https://nanopdf.com/download/comparative-study-of-on-line-algorithms-for-the-elevator-scheduling_pdf

4.https://www.bjmc.lu.lv/fileadmin/user_upload/lu_portal/projekti/bjmc/Contents/8_4_12_Robal.pdf 

A short video that clearly illustrates the problem:
https://www.youtube.com/watch?v=xOayymoIl8U
  
## Offline Algorithm:



