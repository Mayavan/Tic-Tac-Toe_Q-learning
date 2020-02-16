# Import smtplib for the actual sending function
import smtplib

# Send the message via our own SMTP server, but don't include the
# envelope header.
msg = 'Hello world.'

server = smtplib.SMTP('smtp.gmail.com', 587)  # port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('luffyrubberpirateking@gmail.com', '9487785789')
server.sendmail('game.mayavan@gmail.com', 'mayavan95@gmail.com', msg)
server.close()
