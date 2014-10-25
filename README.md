jyproxy
=======

JYProxy is a simple local proxy server that enables web browsers to get around the pornography filtering/blocking that is being done in Korea by the gov't.

### How it works

First, you have to understand how the filtering in Korea works. The filtering device only sees the first part -- to be more exact, HTTP method -- of packets to determine if the packets are HTTP packets and if the device decides that the packets to the target website need to be blocked, it forcibly redirects you to http://warning.or.kr/.

However, by just adding a newline in front of the HTTP method part, the filtering stops working and you will be able to get access to the blocked websites(Yes, ridiculously, adding a newline in front of a HTTP verb works just as fine with so many web servers. See RFC HTTP specs). Which is pretty understandable, considering the fact that adding plenty of exceptions will cause a tremendous decrease in performance for the device.

### How to use

Launch the app(jyproxy.exe), go to the HTTP Proxy setting, and enter localhost:8080. Yes, simple as that.

### Download links

Windows(.exe): [Download](https://dl.dropboxusercontent.com/u/20820651/jyproxy.exe)

EDUCATIONAL PURPOSE *ONLY* 
The author takes no responsibility for any legal problems that using this program can possibly give you. Again, educational purpose *only*.
