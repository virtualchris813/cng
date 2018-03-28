# Custom Name Generator (CNG)
## About CNG
CNG is a Python 2.x application that can be used to generate hostnames via an API call. The hostnames are stored in a PostgreSQL DB. The intention of this project is to provide a naming service that can be used by any Cloud Management Platform (CMP) or other system requiring unique names in a specified format. CNG is provided as a Docker image but you can run it as a standalone Python app if you'd like.

## DISCLAIMER - PLEASE READ! <img src="https://github.com/virtualchris813/cng/blob/master/documentation/Alert.jpg" width="30" height="30" />
### This software is created by me and has no connection to my employer. It is in no way supported or endorsed by VMware. Use this at your own risk, there is no warranty offered or expected!

## Database Requirements
CNG __**does not**__ come with a bundled database. Please install a PostgerSQL database server and provide credentials to CNG. A sample database dump is provided for you to import. The database file is named cng_sql.txt and is in the postgres directory.

## Building the Docker Image
A Dockerfile has been provided in the cng/docker directory. The Docker image will build on Centos:latest and will pull the latest version of the cng application as a tar.gz from the github repo. To build the docker image do the following:<br>
`cd docker`<br>
`docker build -t cng .`<br>
This will create a Docker image named "cng."

## Running CNG via Docker
CNG requires several options to be passed via the docker command line. Here is an example:<br> `docker run -it -e I_LEN="5" -e F_ORDER='hLoc hType hApp dash' -e D_HOST="10.10.10.4" -e D_USER="cng" -e D_PASS="securepass1" -e D_DB="cng" -e D_PORT="5432" -p 5000:5000 cng`
* I_LEN = Incrementor Length - REQUIRED
* F_ORDER = Order of name fields - REQUIRED
* D_HOST = PostgreSQL Host Name or IP - REQUIRED
* D_USER = DB User - REQUIRED
* D_PASS = DB User Password - REQUIRED
* D_DB = Database Name - REQUIRED
* D_PORT = Database Port - OPTIONAL, default is 5432

## Formatting the hostname
The file cng/cng_vars.py contains a full description of fields for the hostname standard being applied. Here is the contents of the notes from that file:<br>
`# This file defines the format of your hostnames`<br>
`# Hostnames can be created in any way you'd like`<br>
`# as long as they follow the format defined in this`<br>
`# file. Examples are provided to assist in the formatting.`<br>
<br>
`# A hostname is made up of several components.`<br>
`# At a minimum you will need one component and`<br>
`# an incrementor defined. Its best to have several`<br>
`# components so the names are somewhat unique but`<br>
`# do as you wish.`<br>
<br>
`# The fields available to build a custom hostname are listed below:`<br>
`#dash       =  A literal dash, "-"`<br>
`#underscore =  An underscore, "_"`<br>
`#hLoc       =  A location code, for example FL (Florida)`<br>
`#hType      =  A system type, for example VM`<br>
`#hApp       =  An application type, for example APP`<br>
`#hUser1     =  A user defined string, whatever you want to fit your naming standard`<br>
`#hUser2     =  A user defined string, whatever you want to fit your naming standard`<br>
`#hUser3     =  A user defined string, whatever you want to fit your naming standard`<br>
`#hUser4     =  A user defined string, whatever you want to fit your naming standard`<br>
`#hUser5     =  A user defined string, whatever you want to fit your naming standard`<br>
`#hIncLength =  The size of the incrementor, for eaxample 3 would result in the 1st being 001`<br>
<br>
`# EXAMPLES`<br>
`# To create hostnames with a format of:`<br>
`# APP TYPE 6 digit incrementor`<br>
`# For example the 23rd web server VM:`<br>
`# WEBVM000023`<br>
` You would define fieldOrder as:`<br>
`# fieldOrder = "hApp hType"`<br>
`# and you would define hIncLength as:`<br>
`# hIncLength = 6`<br>
<br>
`# To create hostnames with a format of:`<br>
`# LOCATION TYPE APP DATACENTER DASH 4 digit incrementor`<br>
`# For example the 5th VM in Florida running an app server in data center 1:`<br>
`# FLVMAPPDC1-0005`<br>
`# You would define fieldOrder as:`<br>
`# fieldOrder = "hLoc hType hApp hUser1 dash"`<br>
`# and you would define hIncLength as:`<br>
`# hIncLength = 4`<br>
<br>
`# To create hostnames with a format of:`<br>
`# ORGINIZATION UNDERSCORE LOCATION UNDERSCORE APP TYPE DASH PROJECT CODE DASH 2 digit incrementor`<br>
`# For example the 2nd web server VM owned by finance in Atlanta on project pg4:`<br>
`# FIN_ATL_WEBVM-pg4-02`<br>
`# You would define fieldOrder as:`<br>
`# fieldOrder = "hUser1 underscore hLoc underscore hApp hType dash hUser2 dash"`<br>
`# and you would define hIncLength as:`<br>
`# hIncLength = 2`<br>

## Example Usage (via curl)
### Requesting a name
`curl -i -H "Content-Type: application/json" -X POST -d '{"name_fields":{"hLoc":"LAB","hType":"VM","hApp":"WEB"}}' http://cng.host.name:5000/cng/api/v0.1/createName`<br>
#### Request Results
`HTTP/1.0 200 OK`
`Content-Type: text/html; charset=utf-8`<br>
`Content-Length: 15`<br>
`Server: Werkzeug/0.11.15 Python/2.7.5`<br>
`Date: Tue, 27 Mar 2018 19:24:34 GMT`<br>
<br>
`labvmweb-000001`<br>
<br>
### Checking if a name already exists
`curl -i -H "Content-Type: application/json" -X POST -d '{"host_name":"labvmweb-000001"}' http://cng.host.name:5000/cng/api/v0.1/queryByName`<br>
#### Query Reults
`HTTP/1.0 200 OK`<br>
`Content-Type: application/json`<br>
`Content-Length: 50`<br>
`Server: Werkzeug/0.11.15 Python/2.7.5`<br>
`Date: Tue, 27 Mar 2018 19:25:15 GMT`<br>
<br>
`{`<br>
`  "Found": true, `<br>
`  "Name": "labvmweb-000001"`<br>
`}`
<br>
### Deleting a name
`curl -i -H "Content-Type: application/json" -X POST -d '{"host_name":"labvmweb-000001"}' http://cng.host.name:5000/cng/api/v0.1/deleteByName`
#### Delete Results
`HTTP/1.0 200 OK`<br>
`Content-Type: application/json`<br>
`Content-Length: 50`<br>
`Server: Werkzeug/0.11.15 Python/2.7.5`<br>
`Date: Tue, 27 Mar 2018 19:30:09 GMT`<br>
<br>
`{`<br>
`  "Found": true, `<br>
`  "Name": "labvmweb-000001"`<br>
`}`
<br>

## To Do
This code is very much a .01 release. There are LOTS of things I plan on doing but here are a few (in no particular order). If you'd like to help or have a suggestion, log an issue or submit a pull request!
* Port to Python 3.
* Add authentication.
* Add SSL Support.
* Put the app behind an NGINX instance.
* Add an update name option.
* Allow the incrementor to be anywhere in the name, it currently must be at the end.
* Cleanup the code, its kind of a mess right now with things in incorrect places.
* Write integration guides for:
  * VMware vRA
  * VMware vRO (initial release of this doc is available)
  * ManageIQ
