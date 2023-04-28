#!/bin/bash
# makes a request from server to catch a respond message
curl -sL -X PUT -H "Origin:School" -d "user_id=98" 0.0.0.0:5000/catch_me
