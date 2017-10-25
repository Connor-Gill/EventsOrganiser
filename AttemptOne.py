import urllib2, json
#import Windows

#print urllib2.urlopen("https://www.cat.com").read()

jsonTest = urllib2.urlopen("https://graph.facebook.com/facebook/picture?redirect=false").read()


print json.loads(jsonTest).values()[0][u"url"]

