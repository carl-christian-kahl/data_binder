import quandl
import pystore
import time

p = "./share/pystore"

pystore.set_path(p)

store = pystore.store('quandl_datastore')

it = 'CHRIS'

# Access a collection (create it if not exist)
collection = store.collection(it)
# List all collections in the datastore
print(store.list_collections())
# returns ['NASDAQ.EOD']

jt1 = 'CME_0D1'
jt2 = 'CME_0D2'

#qd = quandl.get(it + '/' + jt, authtoken='TEbsCbsPnjdCqQCWJzCX')

# Store the data in the collection under AAPL
#collection.write(jt, qd[:-1], metadata={'source': 'Quandl'})

print(collection.list_items())

import time

start = time.time()
df = collection.item(jt1).to_pandas()
end = time.time()

print(end - start)

start = time.time()
df = collection.item(jt2).to_pandas()
end = time.time()

print(end - start)



print(df.head())