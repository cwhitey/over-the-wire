import base64
import binascii

encSecret = "3d3d516343746d4d6d6c315669563362"

print(base64.b64decode(binascii.unhexlify(encSecret)[::-1]))
