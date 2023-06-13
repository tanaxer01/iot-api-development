#!/bin/bash
curl --request PUT http://localhost:5000/location/ed3512d4f6/modify/1 --header 'Content-Type: application/json' \
    --data '{ "name": "fake", "city": "stgo", "country": "chile", "meta": "asdf" }'
