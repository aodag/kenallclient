from kenallclient import KenAllClient

API_KEY = "ebd9446723a8d328a3085f5d359f1e2f14bf4444"

zipcode = "1008105"
client = KenAllClient(API_KEY)
print(client.get(zipcode))
