import base64

def b64AddEquals(b64data):
	b64data += "=" * (-len(b64data) % 4)
	return b64data

def asciiToB64(imagedata):
	b64data = imagedata.decode('ascii')
	b64data = b64AddEquals(b64data)
	return b64data

def writeB64ToFile(b64data, output_path, filename):
	output_file = output_path + '/' + filename

	b64data = b64AddEquals(b64data)
	output_data = base64.urlsafe_b64decode(b64data.encode("ascii"))

	with open(output_file, "wb") as f:
		f.write(output_data)
