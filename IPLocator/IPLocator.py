import pygeoip

geoIP = pygeoip.GeoIP("GeoLiteCity.dat")

ip_address = input("Enter a valid IP Address: ")

res = geoIP.record_by_addr(ip_address)

print("IP Geolocation Data:")
print("-" * 40)
for key, val in res.items():
    print('%s : %s' % (key,val))

print("\n" + "-" * 40)
print("Location:", res['city'], res['region_name'], res['country_name'])
print("Latitude:", res['latitude'])
print("Longitude:", res['longitude'])
print("-" * 40)

input("\nPress any key to exit...")
