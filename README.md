Random Quote Generator
===

## How to Request a quote
  1.	Create a blank text file named: quote-service.txt
  2.	Run quote_generator.py in terminal using the following command: python quote_generator.py
  3.	Send a request using the following command (in python):

        with open(“quote-service.txt”, “w”) as quo_serv:
		quo_serv.write(“quote”)


## How to Receive a quote
  1.	Import time module using the following command: import time
  2.    After sending the request for a quote, wait 1 second using the following command: time.sleep(1)
  3.	To receive the quote use the following command (in python):

  	with open(“quote-service.txt”, “r”) as quo_serv:
  		random_quote = quo_serv.read()
