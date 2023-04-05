#!/bin/bash

export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db
export HBNB_API_HOST=0.0.0.0
export HBNB_API_PORT=5050

echo "Running: python3 api/v1/app.py"
python3 api/v1/app.py

