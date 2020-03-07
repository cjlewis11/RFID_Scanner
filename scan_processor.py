import json

goodscan = "%B6014235005499879=106621629=CHAD/LEWIS=100755894000?;6014235005499879=49121010000001?"
badscan = ";6014235005499879=49121010000001?"
def recieve_rawscan(scaninput):
    #Split our input and verify if its valid.
    parts = scaninput.split("=")
    valid_scan = False
    name = ""
    for item in parts:
        if("/" in item):
            valid_scan = True
            name = item

    #Verify that our scan is correct. Assume its not if it doesn't meet the requirements
    if(not valid_scan):
        return (json.dumps({"Failed":"Rescan"}))

    #If our scan is valid, split the name and verify against the blacklist.
    first,last = name.split("/")
    status = check_blacklist(first.lower(), last.lower())

#Takes in a first and last name
#Checks against the blacklist file
#Returns blacklisted or cleared
def check_blacklist(first, last):
    print("{} {}".format(first,last))
    f = open("blacklist.txt", "r")
    print(f.read())



recieve_rawscan(goodscan)
recieve_rawscan(badscan)


#JSON Packet Framework
# "Success":{
#     "Name": "Marky Mark",
#     "Status": "Blacklisted"
# }
#
# "Failed":"Rescan"
