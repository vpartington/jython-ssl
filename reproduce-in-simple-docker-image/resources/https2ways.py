import traceback
import sys
try:
    import httplib, math, urllib2
    from datetime import datetime

    print "<pre>"
    print "httplib - 1d"
    print

    conn = httplib.HTTPSConnection("www.google.nl")
    print "httplib - 2b"
    print

    conn.request("GET", "/index.html")
    r1 = conn.getresponse()
    conn.close()

    print "urllib2 - 1"
    print

    httpsconn = urllib2.urlopen("https://google.nl")
    print "urllib2 - 2"
    print
    r2 = httpsconn.read()
    httpsconn.close()
except:
    print "Unexpected error:"
    print
    print "0:", sys.exc_info()[0]
    print
    print "1:", sys.exc_info()[1]
    print
    print "2:"
    traceback.print_tb(sys.exc_info()[2], None, sys.stdout)
    print
    print "3:"
    print
    raise
