#!/usr/bin/python2.7
#import library for sending and receiving HTTP messages
import httplib
#collect a host (FQDN) from the user
host = raw_input('\nEnter the domain name of the host you wish to query\n')
#initialize array with basic HTTP(S) request types - GET, POST, etc..
type = ['GET', 'POST']
#host FQDN
connection = httplib.HTTPSConnection(host);
#open connection to host
connection.connect()
#collect a url from the user
url = raw_input('\nEnter the location of the resource, e.x. directory/file/script\n')
#ask user for type of request
chooseType = raw_input('\nEnter 0 for GET, or 1 for POST\n')
#determine request type
requestType = type[int(chooseType)]
#send request to server
connection.request(requestType,'/' + url)
#get response from server, store in variable
response = connection.getresponse()
#read response as a string
stringData = response.read()
#close connection
connection.close()
#print the string to console
print stringData