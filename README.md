# Template E-Mail Sender
*This script reads emails adress from a text file and a message template from another text file, modify the message template using contact data for every contacts in the contact file and sends it.*


### USE
This script uses Message.txt to read message template to make custom messages and Contact.txt to read reciever mail addreses. 

##### Message Template
```
Dear ${PERSON_NAME},

We are happy to inform you that you have been selected for ****** in ${CATAGORY_NAME} category.

Payment procedure:
**** ******


Coupon collection:
Collect your coupon******** the .

Your information: 
Name: ${PERSON_NAME}
Student ID: ${PERSON_ID}
Batch: ${PERSON_BTACH}
Let us know if anything wrong. 
```

##### Contact Template
```
 names, id, batch, email, category   
 Jhon Doe,sd69,B34,xyz@smtp.sce,Advance 
```
