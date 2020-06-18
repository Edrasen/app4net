This project uses multicast UDP sockets to work. 
It needs to handle separately all incomming messages to solve the blocking part of dgram socket,
so there is no problem if you want send and receive messages at the same tame because a thread receive
all the time other users messages.

Chat app notify all users when someone joins and leaves the group.


It needs to add the function of a list of online clients, so we will be working on it in order to improve
UI and give a better UX.

EARM
