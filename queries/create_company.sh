#!/bin/bash
curl --request POST http://localhost:5000/admin/createCompany --header 'Content-Type: application/json' --data '{ "company_name": "test" }'

