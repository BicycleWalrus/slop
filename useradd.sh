#!/bin/bash
# This application is used to create users, and groups!
# It also modifies users to assign them to a group!
# This application consists of three functions: userprompt, createuser, quit
# This application will continue requesting new users/groups to be added until prompted

# userprompt will fetch the new user name and group
userprompt(){
echo "What is the name of our new user?"
read USR
echo "What is the group our new user belongs to?"
read GRP
}

# createuser will run the useradd, groupadd, and usermod functions.
createuser(){
echo "Creating new User!"
sudo useradd $USR
echo "$USR has been created!"
echo "We will now Create $GRP (if necessary) and add $USR to $GRP!"
sleep 1
sudo groupadd $GRP
echo "We will now add $USR to $GRP"
sleep 1
sudo usermod -aG $GRP $USR
echo "Finished!"
}

# quit will determine if the user would like to exit the application after running
quit(){
	echo "Would you like to quit afterwards? (Type exit)"
	read QUT
}

# welcome the user to the application
echo "Welcome to the User/Group Creation Application!"
echo "This application creates users and groups."
echo "This application will also automatically add a user to a group."
echo "This application works with existing groups as well!"
sleep 1

# while loop will run so long as QUT does not equal exit
while [ "$QUT" != "exit" ]
do
	userprompt
	quit
	createuser
done

echo "Thank you for using useradd!"
