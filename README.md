# Custom Name Generator (CNG)
## About CNG
CNG is a small Python 2.x application that can be used to generate hostnames via an API call. The hostnames are stored in a PostgreSQL DB. The intention of this project is to proivide a naming service that can be used by any Cloud Management Platform (CMP) or other system requiring unique names in a specified format. CNG is provided as a Docker image but you can run it as a standalone Python app if you'd like.
CNG does not come with a bundled database. Please install a PostgerSQL database server and provide credentials to CNG. 
