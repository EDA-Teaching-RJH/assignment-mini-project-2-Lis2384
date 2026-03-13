Project Overview
----------------

For this project, i made a management system for contacts. The program lets the you add contacts, view saved contacts, search for a contact by email, update a contact, save contacts to a text file and load them back in when the program starts.


I split the project into three main files:
------------------------------------------

main
models
test contacts

I did this because it made the project easier to organise where main is where the menu and user inputs where ran, models containing the classes and main logic and test contacts where i tested the code.


How my project links to the course material
-------------------------------------------

Object-Oriented Programming:
---------------------------
One of the main things i used in this project was OOP. In models i created the three classes person, contact and contactmanager.
This links to the workshop where we learned about classes and inheritance. My contact class inherits from person, which means i could reuse the code for name and phone instead of writing it multiple times
I used perso for basic details, contact for extra details like email and the date/time created and contactmanager to manage the list of contacts.
This helped make the code more organised and easier to follow. It also showed that i understood how inheritance works.

Regular expressions:
--------------------
Another workshop topic i used was regular expressions. this was one of the most important parts of my project because i used regex to validate both phone numbers and email addresses in the models file.
This links directly to the regex workshop where we learned how to use the re module to check whether the user input matches a pattern. In the workshop, we looked at how regex is better than simple string checking and i used the same idea in my project.
Using regex made the program better because it stops contacts being saved with invalid phone numbers or invalid email addresses.

Testing:
--------
I also used the testing work from the workshops, in test contacts, i used pythons unittest module to test the important part of the program.
This links to the workshop where we moved from simple checks with print() to proper testing using assertions and test files.
Testing was useful because it helped me make sure the code worked without having to keep checking everything manually through the menu.

File I/O:
---------
My project also links to the file handling workshop because it saves and loads data using a text file.
I used the contacts.txt file to store the contact information. When the user adds or updates a contact, the program saves it. When the program starts again, it loads the contacts from the file.
My to_line code changes a contact object into a line of text and from_line turns that saved line back into a contact object.
This part of the project connects to the workshop on file I/O because it uses reading, writing and keeping data after the program has ended.

Libraries:
----------
In this project, i used a few different libraries:
re - was used for regex validation
datetime - was used to store when a contact was created
unittest - was used for testing
tempfile and os - was used in the save/load tests
Using datetime made the project feel a bit more realistic because each contacct stores the time it was added

Comments and readability:
-------------------------
I also used comments in my code to explain what different parts were doing. This links to the workshop where we looked at comments and code readability.
The comments helped me while i was building the project, especially when the code started getting longer and was split across different files. They also make it easier for someone else to understand what each section is doing.

My development process:
-----------------------
I build the project step by step testing each chance i got with unittest.
First i worked on the classes in models so i could get the object structure working and after that i used main to test creating contacts and printing them.
Once that basic structure worked, i added validation using regex for phone numbers and email addresses. After that, I built the contactmanager class so i could store contact, search for them and update them.
When that was working properly, iadded the file saving and loading so the data would stay after the program closed. During this i also had test contacts running at the same time so i was able to test certain features without fully finishing the code.
This way of working felt similar to the workshop style because i started with a basic version and built it up slowly.

Problems i ran into:
--------------------
I had a few problems while making this project.
One issue was putting methods in the wrong class. At one point, i had to_line and from_line in the wrong place, which caused errors when i tried to save contacts. Fixing that helped me understand the structure of the classes better.
Another issue was inheritance. I forgot to include super(). _init_ (name, phone) in the contact class at first, which meant the inherited data was not being set properly, once i fixed that, the class worked as expected.
I also had problems with file handling when contacts.txt did not exist yet. I fixed that by using try and except filenotfounderror so the file could be created if needed.
There were also a few errors where the format for saving contacts did not match the format for loading them. i fixed that by making sure to_line and from_line used the same order and the same separator.
These mistakes were annoying while i was doing them, but they did help me understand the code better in the end.

What Went Well:
---------------
I think the strongest part of my project is that it brings together different topics from the course in one program.
parts i think went well:
-using classes properly
-using inheritance
-validating phone and emails with regex
-saving and loading from text file
-testing the code in a separate file
-splitting the project into multiple files

I think this made the project feel more complete and more like a proper small application rather than just one short task

What i would improve:
---------------------
I would mainly improve of phone validation. At the moment it accepts a wide range of phone formats, but i could make it stricter by only allowing specific area codes or something along these lines
Also during adding, updating i should have made it so that if you got an incorrect email or phone, it wont wait till the end to tell you that it is invalid.

Conclusion
----------
Overall this project helped me combine different python topics into one working system. Instead of learning classes, regex, testing and file handling seperately, this project made me use them together.
The workshops were useful because each one helped with a different part of the project. The regex workshop helped with validation, the class workshop helped with structure and inheritance, the testing workshop helped with writing the test file and the file I/O workshop helped with saving and loading data.
I think this project gave me a better understanding of how these topics work together in a real program and also showed me how to fully build a code and carefully test as i go. 
