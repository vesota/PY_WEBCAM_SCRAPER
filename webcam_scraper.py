import urllib
import time

span = 86400
anz_bil = span/15

for n in range (anz_bil):
    n + 15
    time.sleep(10)
    #resource = urllib.urlopen("http://webcam.toblach.info/webcam.asp")
    resource = urllib.urlopen("http://live.tyrol.at/tyrolcams/innsbruck/ibk2/ibk2.php?1404941219286")
    
    time1 = time.asctime()
    time2 = time1.replace(":", "")
    timeext = time2.replace("2015", ".jpg")
    filename = ''.join(timeext.split())
    print filename

    output = open(filename,"wb")
    output.write(resource.read())
    output.close()
    
