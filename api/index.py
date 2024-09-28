from flask import Flask, request, jsonify
import random, binascii, zlib

class FST:
	__tmp_bfuo = "suSyjnofjUTddCgifjks=="
	__tmp_dmucy = "fifigkzhdizyzudZidudYdud=="
	__tmp_cs = "hprshEckFifafifUDUdwuroc="
	__tmp_gts = "dgihciArinophv";
	__tmp_iow = "pohnWOMarQonnbgyiBnvzKe=="
	__tmp_aukb = "pihvaqripavWHo+GidhbVchj="
	__tmp_ewq = "gncBsrilSNKxgvSvjkkn="
	__tmp_wimbato = "YdVklodsvjooaSryjnnVjRf"
	__j = 10
	__k = 23
	__m = 98
	__o = 54
	__h = 19
	def decode(self, ciphertext):
		try:
			key = self.__tmp_bfuo[10]+self.__tmp_iow[9]+self.__tmp_gts[6]+self.__tmp_aukb[11]+self.__tmp_ewq[3]+self.__tmp_cs[5]+self.__tmp_dmucy[20]+self.__tmp_wimbato[21]+self.__tmp_bfuo[10]
		
			key_bytes = binascii.b2a_base64(key.encode(), newline=False)
		
			ciphertext_bytes = bytearray.fromhex(ciphertext)
		
			decompressed_bytes = bytearray()
			for i, b in enumerate(ciphertext_bytes):
				decompressed_bytes.append(b ^ key_bytes[i % len(key_bytes)])
		
			plaintext_bytes = zlib.decompress(decompressed_bytes)
			return binascii.a2b_base64(plaintext_bytes).decode()
		except:
			return ""
	
	def encode(self, plaintext):
		try:
			key = self.__tmp_bfuo[10]+self.__tmp_iow[9]+self.__tmp_gts[6]+self.__tmp_aukb[11]+self.__tmp_ewq[3]+self.__tmp_cs[5]+self.__tmp_dmucy[20]+self.__tmp_wimbato[21]+self.__tmp_bfuo[10]
			key_bytes = binascii.b2a_base64(key.encode(), newline=False)
			plaintext_bytes = binascii.b2a_base64(plaintext.encode(), newline=False)
		
			compressed_plaintext = zlib.compress(plaintext_bytes)
		
			ciphertext_bytes = bytearray()
			for i, b in enumerate(compressed_plaintext):
				ciphertext_bytes.append(b ^ key_bytes[i % len(key_bytes)])
		
			return binascii.b2a_hex(ciphertext_bytes).decode()
		except:
			return ""

fst = FST()
encode = fst.encode
decode = fst.decode

app = Flask(__name__)

def validate(key):
	apr_keys = [
		"23EzXw8VNfRzX58VdfBzXf9VYfVzX08VOfle23AUQ10UxEzMz00TO90QUFDOxAjMwATNfle"
	]
	return key in apr_keys

def get_rand(length):
	chars = ["o", "O", "0"]
	result = ""
	for _ in range(length):
		random_index = random.randint(0, len(chars) - 1)
		result += chars[random_index]
	return result

def is_exist(out, ok, ov):
	for k, v in out.items():
		if k == ok and v == ov:
			return True
	return False

def resp(l, ok=False, ov=False):
	out = {}
	u = random.randint(120, 180)
	d = False
	for i in range(l):
		if ok and ov and u == i and not d:
			out[ok] = ov
			d = True
		key = get_rand(random.randint(20, 30))
		value = get_rand(random.randint(60, 110))
		out[key] = value
	if ok and ov and not is_exist(out, ok, ov):
		out[ok] = ov
	return out

@app.route("/status", methods=["GET", "POST"])
def api_state():
	st_key = "0Oooo0oOo0000OOooO0o0OO0OOOOOoOOO00O00OO0ooO0OO00O"
	st_value_on = "o00o0OoOO0OoOooo0oO00O00oooooO0o0oo0Oooo0o00O0OOoO0oOO0O00O0o00o0O0O0oo00OOo0oOo00Oo0OOoOoOO00oo0oO00O0ooo0000oOooooOOO0o0oooO0oo0"
	st_value_off = "o0o0oOOOoO0o0O0o000O0O0o0Oo00OO0OO00OO0oO0O0o0Oo000OoO0OO0o0000oO0O0ooo0O0OOO0Oo0OOo0OOooOooOoO0OoO00OO00OoOOOooO0oo0000ooO0O0o0o0"
	st_value_dev = "000o0oOO00o00O0OooO000oOO0oOOo0OoOOOOOOoo00ooOo0oo0O0o000Oo0o00oOOo0OoOOO00O00o0ooOO0oO00O00ooo000o000oOo0o0OOO0oOo0Oo00O0O0oo0OoO"
	
	
	o = {st_key: st_value_on}
	out = resp(random.randint(100, 200), st_key, st_value_on)
	out = dict(o, **out)
	out[st_key] = st_value_on
	return encode(str(out)), 200

@app.route("/", methods=["GET", "POST"])
def api():
	if request.method == "GET":
		out = resp(random.randint(100, 200))
		return encode(str(out)), 200

	if request.method == "POST":
		op_key = "OoOOoOo0oO0o0o0oOOoooOO0ooO0o0oo0OoOOooo"
		op_value_i = "0oOo00oO0o00oo0O000OO0ooooOO0o0ooooO00000o0o00ooO0000Ooo0ooO0o0ooOOoooOoooo0000o00oOo0000oOo0OOooooOO00Ooo0o0O0O00000o0o"
		try:
			key = decode(request.headers.get("Android-Id")) + decode(request.form["android-id"])
		except:
			key = ""
		if key == "":
			o = {op_key: op_value_i}
			out = resp(random.randint(100, 200), op_key, op_value_i)
			out = dict(o, **out)
			out[op_key] = op_value_i
			return encode(str(out)), 200

		if validate(key):
			op_value_v = "oOOOooOOo0O000OooOOOo0o0oO00o00OoOOooOOoOOOO0oOOOoOooooO00oooOOoooOo0000o000O000oOo0o00Oo0OO0oOooOOo0oOoO00OOOO0Oo0OOOOO"
			o = {op_key: op_value_v}
			out = resp(random.randint(100, 200), op_key, op_value_v)
			out = dict(o, **out)
			out[op_key] = op_value_v
			return encode(str(out)), 200
		else:
			o = {op_key: op_value_i}
			out = resp(random.randint(100, 200), op_key, op_value_i)
			out = dict(o, **out)
			out[op_key] = op_value_i
			return encode(str(out)), 20
