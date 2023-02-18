# snake_pi
Code running on a pi for snake room temps back up to faunadb

# Setting Up Pre-Req's
Ensure you have the below installed on the pi:

`sudo apt-get install python3-dev python3-pip`

Also ensure we update pip and setuptools

`sudo python3 -m pip install --upgrade pip setuptools wheel`

Now install the Adafruit DHT Package:

`sudo pip3 install --install-option="--force-pi" Adafruit_DHT`

# Fauna Access Key
You will need to get an access key for the faunadb after you setup the db and then export that via:

`export FAUNA_KEY=xxxxxx`

Then after installing pre-req's mentioned above you can run:

`python snake_temp.py` to have it check the temp and send it plus the time up to the graphQL endpoint of the faunadb.