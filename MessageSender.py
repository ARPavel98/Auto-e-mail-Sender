import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#My mail info
MY_ADDRESS = 'mailHere@gmail.com'
PASSWORD = 'passwordHere'

#Read the contacts 
def get_contacts(filename):
    names = []
    id = []
    batch = []
    emails = []
    catagory = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(',')[0])
            id.append(a_contact.split(',')[1])
            batch.append(a_contact.split(',')[2])
            emails.append(a_contact.split(',')[3])
            catagory.append(a_contact.split(',')[4])
    return names, id, batch, emails, catagory

#Read the template measage 
def read_template(filename):
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    names, ids, batchs, emails, catagories = get_contacts('contacts.txt') 
    message_template = read_template('message.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    
    for name, id, batch, email, catagory in zip(names, ids, batchs, emails, catagories):
        msg = MIMEMultipart()      
        print(name)
        print(email)
        print(catagory)
        
        message = message_template.substitute(PERSON_NAME=name,CATAGORY_NAME=catagory, PERSON_ID=id, PERSON_BTACH=batch)
       

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="SEU_Intra University Programming Contest 2k19 Confirmation"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
