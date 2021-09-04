import os
import json

#Hi guys this is a example for using files
#===========================================================

def read_api_from_web():
    fPath="./API"
    listOfFoldder = os.listdir(fPath)
    fName = listOfFoldder[0]
    # print(listOfFoldder[0])
# get the first file name as a string
    info = open(f'{fPath}/{fName}',)
    info = json.load(info)[0] # remove list leave only dict
    print(info["pk"])
    print(info["fields"])
    print("========================")
    print(info["fields"]["user_id"])
    print(info["fields"]["satellite_id"])
    print(info["fields"]["begin"])
    print(info["fields"]["end"])
    # get only what you need full dict is 
    # {"model": "booking.booking", "pk": 21, "fields": {"user_id": 1, "satellite_id": "dsa", "begin": "2021-09-11T19:06:00Z", "end": "2021-09-25T19:06:00Z"}}
    #to access second dict just add info[fileds] before what you need

def write_api_from_raps():
    fPath="./API"
    listOfFoldder = os.listdir(fPath)
    fName = listOfFoldder[0]
    info = open(f'{fPath}/{fName}',)
    info = json.load(info)[0] # remove list leave only dict
    #this can probally probably be  global
    rapsDict = {"booking_id":info["pk"], "waterfall":'data you get from rasp', "decoded":'data', "processed":'data'}
   
    f = open(f'{fPath}/{fName[:-8:]}in.json', 'w')
    f.write(f'{rapsDict}\n')
    f.close()


read_api_from_web()
write_api_from_raps()