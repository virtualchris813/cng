# Custom Name Generator (CNG)
## About CNG
CNG is a small Python 2.x application that can be used to generate hostnames via an API call. The hostnames are stored in a PostgreSQL DB. The intention of this project is to proivide a naming service that can be used by any Cloud Management Platform (CMP) or other system requiring unique names in a specified format. CNG is provided as a Docker image but you can run it as a standalone Python app if you'd like.
## Database Requirements
CNG __**does not**__ come with a bundled database. Please install a PostgerSQL database server and provide credentials to CNG. 

## Running CNG via Docker
CNG requires several options to be passed via the docker command line. Here is an example: `docker run -it -e I_LEN="5" -e F_ORDER='hLoc hType hApp dash' -e D_HOST="10.10.10.4" -e D_USER="cng" -e D_PASS="securepass1" -e D_DB="cng" -e D_PORT="5432" -p 5000:5000 cng`
* I_LEN = Incrementor Length - REQUIRED
* F_ORDER = Order of name fields - REQUIRED
* D_HOST = PostgreSQL Host Name or IP - REQUIRED
* D_USER = DB User - REQUIRED
* D_PASS = DB User Password - REQUIRED
* D_DB = Database Name - REQUIRED
* D_PORT = Database Port - OPTIONAL, default is 5432
