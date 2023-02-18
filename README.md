# snake_pi
Code running on a pi for snake room temps back up to faunadb

# Fauna Access Key
You will need to get an access key for the faunadb after you setup the db and then export that via:

`export FAUNA_KEY=xxxxxx`

Then after installing pre-req's mentioned above you can run:

`python snake_temp.py` to have it check the temp and send it plus the time up to the graphQL endpoint of the faunadb.