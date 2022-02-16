# Microbrewery

Imagine that you are part of a microbrewery that wants to consolidate their systems using a microservices approach. The goal of the project is to create a single API that seamlessly exposes the data of three different systems: Warehouse, Accounting, Sales.

# Files structure
.  
├── accounting  
│ ├── accounting.py  
│ ├── accounts.json  
│ └── Dockerfile  
├── api  
│ ├── app.py  
│ └── Dockerfile  
├── docker-compose.yml  
├── makefile  
├── requirements.txt  
├── sales  
│ ├── Dockerfile  
│ ├── sales.json  
│ └── sales.py  
├── setup.py  
├── tests  
│ ├── accounting.test.py  
│ ├── sales.test.py  
│ └── warehouse.test.py  
└── warehouse  
├── beers.json  
├── Dockerfile  
└── warehouse.py

## Run

`sudo make launch`
or
`sudo docker-compose up --build -d`
For sales
`http://0.0.0.0:5000/sales`
`http://0.0.0.0:5000/sales/john`
For accounts
`http://0.0.0.0:5000/accounts`
`http://0.0.0.0:5000/sales/abinash`
For warehouse
`http://0.0.0.0:5000/warehouse/beers`
`http://0.0.0.0:5000/warehouse/beer/carlsberg`

## Shutdown

`sudo make shutdown`
or 
`sudo docker-compose down`

## TODO
- NGINX
- CI/CD