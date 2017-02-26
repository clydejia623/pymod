import urllib2
import requests
import json
import md5
import datetime
import base64

''' request tools test'''
def Requests_Get_test():
    url = "https://api.ucpaas.com/2014-06-30/"
    para = {"p1":"1","p2":"2"}
    dat = {"j1":"aaa","j2":"bbb"}
    try:
        #r = requests.get(url,params=para)
        r = requests.get(url)
    except:
        print "get failed"
        return False
    print r.url
    #print r.text
    #print r.encoding
    #print r.content
    print r.status_code
    
def Request_Post_test():
    url = "http://httpbin.org/post"
    dat = {"pa":"1","pb":"2"}
    try:
        r = requests.post(url,dat)
    except:
        print "post error"
        return False
    print r.url
    print r.status_code
    #print r.text
    print r.json

'''ucpaas test use HTTP request tools'''
def CreateClientJson():
    r = {}
    c = {}
    c["clientType"] = "0"
    c["appId"] = "cd27257cbb464215ba86c878e91b2d79"
    c['charge'] = 0
    r["client"] = c

    return r

#
def GetUcpaasUserinfo():
    #url = "https://api.ucpaas.com/2014-06-30/Accounts/53a6909c297a59a42a71cfe59d9464b8/Clients.json"
    url = "https://api.ucpaas.com/2014-06-30/Accounts/53a6909c297a59a42a71cfe59d9464b8"
    sid = "53a6909c297a59a42a71cfe59d9464b8"
    
    #sig
    token = "9f46b96ceb4e11025d06460945e97da1"
    now = datetime.datetime.now()
    timestemp = now.strftime("%Y%m%d%H%M%S")
    print timestemp
    sigstr = sid + token + timestemp
    sig = md5.new(sigstr).hexdigest().upper()
    print sig
    
    para = {}
    para['sig'] = sig
    
    #auth
    src = sid + ":" + timestemp
    auth = base64.encodestring(src).strip()
    print auth
    
    dat = CreateClientJson()
    print dat
    hdrs = {}
    hdrs["Accept"] = "application/json"
    hdrs["Authorization"] = auth
    hdrs["Content-Type"] = "application/json;charset=utf-8"
    hdrs["Content-Length"] = "0"
    
    #r = requests.get(url,params=para,data=dat,headers = hdrs)
    r = requests.get(url,params=para,headers = hdrs)
    print r.url
    print r.status_code
    #print r.raw
    print r.content
    #print r.headers
    return True

def CreateUcpaasClient():
    #url = "https://api.ucpaas.com/2014-06-30/Accounts/53a6909c297a59a42a71cfe59d9464b8/Clients.json"
    url = "https://api.ucpaas.com/2014-06-30/Accounts/53a6909c297a59a42a71cfe59d9464b8/Clients.json"
    sid = "53a6909c297a59a42a71cfe59d9464b8"
    
    #sig
    token = "9f46b96ceb4e11025d06460945e97da1"
    now = datetime.datetime.now()
    timestemp = now.strftime("%Y%m%d%H%M%S")
    print timestemp
    sigstr = sid + token + timestemp
    sig = md5.new(sigstr).hexdigest().upper()
    print sig
    
    para = {}
    para['sig'] = sig
    
    #auth
    src = sid + ":" + timestemp
    auth = base64.encodestring(src).strip()
    print auth
    
    dat = CreateClientJson()
    print dat
    hdrs = {}
    hdrs["Accept"] = "application/json"
    hdrs["Authorization"] = auth
    hdrs["Content-Type"] = "application/json;charset=utf-8"
    hdrs["Content-Length"] = "%s" % (json.dumps(dat))
    
    #r = requests.get(url,params=para,data=dat,headers = hdrs)
    r = requests.post(url,params=para,data = json.dumps(dat),headers = hdrs)
    print r.url
    print r.status_code
    #print r.raw
    print r.content
    #print r.headers
    return True    
def CreateVSMSJson():
    r = {}
    c = {}
    c["to"] = "13751110116"
    c["appId"] = "cd27257cbb464215ba86c878e91b2d79"
    c['verifyCode'] = "223344"
    r["voiceCode"] = c

    return r
def UcpaasSendVSMS():
    #url = "https://api.ucpaas.com/2014-06-30/Accounts/53a6909c297a59a42a71cfe59d9464b8/Clients.json"
    url = "https://api.ucpaas.com/2014-06-30/Accounts/53a6909c297a59a42a71cfe59d9464b8/Calls/voiceCode"
    sid = "53a6909c297a59a42a71cfe59d9464b8"
    
    #sig
    token = "9f46b96ceb4e11025d06460945e97da1"
    now = datetime.datetime.now()
    timestemp = now.strftime("%Y%m%d%H%M%S")
    print timestemp
    sigstr = sid + token + timestemp
    sig = md5.new(sigstr).hexdigest().upper()
    print sig
    
    para = {}
    para['sig'] = sig
    
    #auth
    src = sid + ":" + timestemp
    auth = base64.encodestring(src).strip()
    print auth
    
    dat = CreateVSMSJson()
    print dat
    hdrs = {}
    hdrs["Accept"] = "application/json"
    hdrs["Authorization"] = auth
    hdrs["Content-Type"] = "application/json;charset=utf-8"
    hdrs["Content-Length"] = "%s" % (json.dumps(dat))
    
    #r = requests.get(url,params=para,data=dat,headers = hdrs)
    r = requests.post(url,params=para,data = json.dumps(dat),headers = hdrs)
    print r.url
    print r.status_code
    #print r.raw
    print r.content
    #print r.headers
    return True    
    return False


if __name__ == "__main__":
    #Requests_Get_test()
    #Request_Post_test()
    #CreateClientJson()
    #CreateUcpaasClient()
    UcpaasSendVSMS()