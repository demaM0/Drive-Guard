import bluetooth
def search():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)  
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        f = open("myfile.txt", "w")
        f.write(" %s - %s" % (addr, name))
        f.close()
        print(" %s - %s" % (addr, name))
    return nearby_devices
    