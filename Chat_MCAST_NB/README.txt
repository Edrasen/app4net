This project uses multicast UDP sockets to work. 
It needs to handle separately all incomming messages to solve the blocking part of dgram socket,
so there is no problem if you want send and receive messages at the same tame because a thread receive
all the time other users messages.

Chat app notify all users when someone joins and leaves the group.

-------- FINAL -------

Now chat lets select a specific user to chat with or chat with all members on the group.

Users list is send using rpyc through localhost by remote procedure call.


EARM
