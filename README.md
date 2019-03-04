# week7-CA
## Certificate Authority Assignment
### Running the software
In order to run the software, you will need to start up myServer.py and myCA.py before you start myClient.py. Failure to do so in this order will result in an error that states the machine has actively refused the connection.
### Problems with the program
As you run this, you will notice that it seems slow. It takes (what feels like) a minute before the software returns its responses from the CA server.
Somewhere, somehow, the server is losing the data and I can't find it. When I have a fresher mind and I'm not worried about getting other things done, I will walk right up to it and find the bug. Right now, though, it's just not popping out at me.
### Encryption method used
I used a simple substitution cipher that takes a string and outputs its numeric position in the alphabet.
### Answers to the assignment questions
1. Hours spent in completing this assignment, once again, topped 25 or more. I experienced the same frustration that Jay Hubert experienced in that I didn't pick up on a clear way of getting to the end-product from the videos. The discussion, however, was extremely helpful when Joseph Lister laid out what was necessary with each file. From there, I was able to put a flowchart together and started working on each step individually with baby functions. Once I got those going, it was just a matter of debugging it. Unfortunately, the revelation of baby steps didn't come to me until about 6:00 tonight (Sunday) so....
2. The most straightforward part of the tasks is a tie between 1) creating the socket or 2) writing the encryption algorithm. I spent a lot of time on RSA and other encryptiong certification methodologies and couldn't get them to work, so I wrote my own.
3. The most frustrating technical challenge was trying to get the cryptology objects to work like cryptology objects in my mind. When I couldn't do that (example: RsaKey doesn't have len), then I wrote my own to overcome it.
4. I have been fascinated by cryptography since college. In junior high, I tried to develop an algorithm that would produce nothing but prime numbers. By the time I took my ASVAB, I had finished in the 99th percentile for the cryptology section. It has always fascinated me.
5. As a masters candidate, I understand that it shouldn't be necessary to spoon-feed me how to do these assignments. I should be quite capable of putting together the information from the assignments and the Python documentation to make it work. These last two weeks have been absolute nightmares for me in trying to get this stuff done. So, to answer the question, the magic piece of documentation would show me sample code of how this all comes together or the flowcharting for this. I couldn't get off the starting line until I saw Lister's post to Hubert.
