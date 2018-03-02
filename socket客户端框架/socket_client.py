# _*_coding:utf-8_*_
# Author:xupan
import socket
import select

class Request():
	def __init__(self,sock,info):
		self.sock=sock
		self.info=info

	def fileno(self):
		return self.sock.fileno()

class GClient():
	def __init__(self):
		self.sock_list=[]
		self.conns=[]

	def add_request(self,req_info):
		sock=socket.socket()
		sock.setblocking(False)

		try:
			sock.connect((req_info['host'],req_info['port']))
		except BlockingIOError as e:
			pass

		obj=Request(sock,req_info)
		self.sock_list.append(obj)
		self.conns.append(obj)

	def run(self):
		while True:
			#监听
			r,w,e=select.select(self.sock_list,self.conns,[],0.05)

			#w 是否连接成功
			for obj in w:
				data="GET %s HTTP/1.1\r\nhost:%s\r\n\r\n" %(obj.info['path'],obj.info['host'])
				obj.sock.send(data.encode('utf-8'))
				self.conns.remove(obj)

			#r 是否有返回值
			for obj in r:
				response=obj.sock.recv(8096)
				obj.info['callback'](response)
				self.sock_list.remove(obj)

			#如果所有都有返回值，就断开
			if not self.sock_list:
				break



################################
def done1(response):
	print(response)


def done2(response):
	print(response)

url_list=[
	{'host': 'www.baidu.com', 'port': 80, 'path': '/', 'callback': done1},
	{'host': 'www.cnblogs.com', 'port': 80, 'path': '/index.html', 'callback': done2},
	{'host': 'www.bing.com', 'port': 80, 'path': '/', 'callback': done2},
]

GClient=GClient()
for item in url_list:
	GClient.add_request(item)

GClient.run()