# follow these instructions:
# Create a seed.sh file in your project directory
# Place the code below in the file.

#!/bin/bash
rm -rf wineadventureapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations wineadventureapi
python3 manage.py migrate wineadventureapi

python3 manage.py loaddata user
python3 manage.py loaddata category
python3 manage.py loaddata wines
python3 manage.py loaddata wines101
python3 manage.py loaddata wine_category


# Run chmod +x seed.sh in the terminal.
# run ./seed.sh in the terminal to run the commands
