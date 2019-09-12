import urllib2, time
hosts = "http://yahoo.com", "http://google.com", "http://ibm.com", "http://apple.com"
start = time.time()
for host in hosts:
    print(host)
    url_loc = urllib2.urlopen(host)
    print(url_loc.read(1024))
print("Elapsed Time: %s" % (time.time()-start))