from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log

import sys
log.startLogging(sys.stdout)

class ProxyClient(proxy.ProxyClient):
    def handleHeader(self, key, value):
        proxy.ProxyClient.handleHeader(self, key, value)
    def handleResponsePart(self, buffer):
        proxy.ProxyClient.handleResponsePart(self, buffer)

class ProxyClientRequest(proxy.ProxyClientFactory):
    protocol = ProxyClient 

class ProxyRequest(proxy.ProxyRequest):
    protocols = dict(http=ProxyClientRequest)
    def process(self):
        # This avoids the filtering (so dumb) 
        self.method = '\r\n' + self.method
        proxy.ProxyRequest.process(self)

class ProxyProtocol(proxy.Proxy):
    requestFactory = ProxyRequest 

class ProxyFactory(http.HTTPFactory):
    protocol = ProxyProtocol 

reactor.listenTCP(8080, ProxyFactory())
reactor.run()
