from xlrd import open_workbook
from random import randint
#wb = open_workbook('/home/user/Downloads/AWCData_DSB.xlsx')
#print wb
dict_keys = ['','zone_name','state_name','district_name','revenue_division','mandal_name','village_name','institute_type','awc_code','awc_name','pincode','aww_name','children_total','awc_incharge_name','mobile_number','ward_number']

# for sheet in wb.sheets():
#     #print sheet
#     number_of_rows = sheet.nrows    
#     number_of_columns = sheet.ncols
#     print number_of_columns,"dfdfd"

#     for row in range(1,number_of_rows):
#         rowlist={}
#         for col in range(2,number_of_columns):            
#             rowlist[dict_keys[col]] =(sheet.cell(row,col).value)
#         try:
#             loc_obj = Locations.objects.get(**rowlist)
#         except Exception as e:
#             loc_obj = Locations.objects.create(**rowlist)


kwargs = {
    "state_name":"rathna",
    "zone_name":"zone 1"
}


def get_district(**kwargs):
    print kwargs
    pass

get_district(**kwargs)


# from zeep import Client
# import zeep
# wsdl = 'http://geo.dot.ca.gov/services/PostmileWebService?wsdl'
# #client = zeep.Client(wsdl=wsdl)
# #print client
# client = Client(wsdl)
# print client

#result = client.service.ConvertSpeed(
    #100, 'kilometersPerhour', 'milesPerhour'
#print(client.service.complexType)


        
# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)

# print random_with_N_digits(10)
#import the WSDL module, this does all the work for you.
from SOAPpy import WSDL
from xml.dom import minidom
#specify the wsdl file. This file contains everything an application needs to know
#to call the service with the right arguments, with the right protocol at the right
#location etc.
WSDLFile   = "https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl"

#Create a proxy. You can call methods that are on a distant machine as if they were
#on your local machine, as if they were implemented in the proxy object.

proxy   = WSDL.Proxy(WSDLFile)
#print proxy
print proxy.methods.keys()
#uncomment thoses lines to see outgoing and incoming soap envelops
#proxy.soapserver.config.dumpSOAPIn=1
#proxy.soapserver.config.dumpSOAPOut=1

Centigrades = 12

#Here we call the action CtoF as if were a method defined in the proxy object.
Faranheites  = proxy.LatLonListZipCode(zipCodeList="99501")
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring
myxml = ET.fromstring(Faranheites)
for each in myxml:
	print each.text

#print "%s Centigrades = %s Faranheites" % (Centigrades,Faranheites)

# from SOAPpy import WSDL

# #The location of our webservice description
# #WSDLFile = "http://geo.dot.ca.gov/services/PostmileWebService?wsdl"
# WSDLFile = "http://currencyconverter.kowabunga.net/converter.asmx"

# #Object to handle the requests and responses from our
# #webservice
# proxy = WSDL.Proxy(WSDLFile)

# #This will print the documentation of the Proxy class
# #print proxy.__doc__
# #This will print all the available methods and parameters
# #in the webservice
# print proxy.methods.keys()

# #Some of the properties of the SOAP object.
# # print proxy.soapproxy.namespace
# # print proxy.soapproxy.soapaction
# # print proxy.wsdl

# #You can use this to access each method
# #of the webservice.
# #for method in proxy.methods.keys() :
# # ci = proxy.methods[method]
# # for param in ci.outparams :
# # print param.name.ljust(20) , param.type

# currencies = proxy.ListActiveCurrencies()

# #This will print the XML returned by the webservice
# print(currencies)
        

