# -*- coding: utf-8 -*-
"""
python-bna
Battle.net Authenticator routines in Python.

Specification can be found here:
  <http://bnetauth.freeportal.us/specification.html>
Python implementation by Jerome Leclanche <j.leclanche@gmail.com>
"""
from time import time
from hashlib import sha1

RSA_KEY = 104890018807986556874007710914205443157030159668034197186125678960287470894290830530618284943118405110896322835449099433232093151168250152146023319326491587651685252774820340995950744075665455681760652136576493028733914892166700899109836291180881063097461175643998356321993663868233366705340758102567742483097
RSA_MOD = 257


def getEmptyEncryptMsg(otp, region, model):
	ret = (otp + "\0" * 37)[:37]
	ret += region or "\0\0"
	ret += (model + "\0" * 16)[:16]
	return chr(1) + ret

def doEnroll(data, enroll_host="mobile-service.blizzard.com", enroll_uri="/enrollment/enroll.htm"):
	"""
	Send computed data to Blizzard servers
	Return the answer from the server
	"""
	from httplib import HTTPConnection
	
	conn = HTTPConnection(enroll_host)
	conn.request("POST", enroll_uri, data)
	response = conn.getresponse()
	
	if response.status != 200:
		raise IOError("%s returned status %i" % (enroll_host, response.status))
	
	ret = response.read()
	conn.close()
	return ret

def encrypt(data):
	data = int(data.encode("hex"), 16)
	n = data ** RSA_MOD % RSA_KEY
	ret = ""
	while n > 0:
		n, m = divmod(n, 256)
		ret = chr(m) + ret
	return ret

def decrypt(response, otp):
	return "".join(chr(ord(c) ^ ord(e)) for c, e in zip(response, otp))

def requestNewSerial(region="US", model="Motorola RAZR v3"):
	"""
	Requests a new authenticator
	This will connect to the Blizzard servers
	"""
	def timedigest(): return sha1(str(time())).digest()
	
	otp = (timedigest() + timedigest())[:37]
	data = getEmptyEncryptMsg(otp, region, model)
	
	e = encrypt(data)
	response = decrypt(doEnroll(e)[8:], otp)
	
	secret = response[:20]
	serial = response[20:]
	
	region = serial[:2]
	if region not in ("EU", "US"):
		raise ValueError("Unexpected region: %r" % (region))
	
	return {"serial": serial, "secret": secret}

def getToken(secret, digits=8):
	"""
	Gets the current token for a given secret
	"""
	import hmac
	from struct import pack, unpack
	t = int(time())
	msg = pack(">Q", t / 30)
	r = hmac.new(secret, msg, sha1).digest()
	idx = ord(r[19]) & 0x0f
	h = unpack(">L", r[idx:idx+4])[0] & 0x7fffffff
	return h % (10 ** digits)
