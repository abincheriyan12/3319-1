Abin Cheriyan
CIS 3319
                                        Lab Report 1


In this Lab, I learned how to do basic encryption and socket programming. 
I never really code on python, but for this project i taught myself how to use 
pycharm and code in python (Python is much easier than C and Java). 
I also had to read up on socket programming on python since i never really
 did a lot of socket programming or any encryption before, so that took some time.


Steps:
* Implemented and imported DesKey into Pycharm using the plugins function. I was unable to establish a connection between the server and the client before importing the DesKey.
* I had to create my text file for it to be read in as the key that would be generated and used in both the client and the server. I named it “key”
* I then had to create the sockets for both the client and the server. I named it clientside.py and serverside.py
* After this step, I knew we needed to take a string in and had to keep taking a string in till something stops, so i created a while (true)  statement that just confirmed that as long as there was a connection established between the client and the server, the user using the program would be able to type their message.
* After you type the message in and the read function reads in the string, I used the key established from the text file I created, to be able to encode their message in ‘utf-8’. 
* Since both the serverside and the clientside is almost similar, I knew i could just copy basically what I wrote from the clientside.py file to the serverside.py file and  was able to encrypt/decrypt the ciphertext once the string/ word message was entered.
