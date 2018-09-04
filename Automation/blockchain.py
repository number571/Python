from os import curdir, listdir, mkdir
from os.path import isdir

from json import dump, loads
from hashlib import sha512

EXTEN_JSON = lambda: ".json"
ZERO_BLOCK = lambda: "0.check"
BLOCKCHAIN = lambda: curdir + "/Blockchain/"

head = lambda xs: xs[0]  # -> int
tail = lambda xs: xs[1:] # -> list

full_path = lambda x: BLOCKCHAIN() + x # -> str
open_file = lambda x: open(full_path(str(x) + EXTEN_JSON()), "rb").read() # -> str

get_hash  = lambda x: sha512(open_file(x)).hexdigest() # -> str
get_json  = lambda x: loads(open_file(x))['hash'] # -> str
get_state = lambda x, y: [{"file": str(x-1) + EXTEN_JSON(), "state": y}] # -> list

sort_blocks = lambda xs: sorted(tuple(map(lambda z: int(z.split(".")[0]), listdir(xs)))) # -> list
last_block  = lambda x: sort_blocks(x)[-1] # -> int

def checkBlocks(List) -> list:
	if not List: return []
	elif get_hash(head(List) - 1) != get_json(head(List)): \
		  return get_state(head(List), False) + checkBlocks(tail(List))
	else: return get_state(head(List), True ) + checkBlocks(tail(List))

def checkEndBlock(end, zero) -> list:
	if get_hash(end) != open(full_path(zero)).read():
		  return get_state(end + 1, False)
	else: return get_state(end + 1, True )

def checkIntegrity(path, zero) -> list:
	return checkBlocks(sort_blocks(path)[2:]) + checkEndBlock(last_block(path), zero)

def checkDir(path) -> bool:
	if path not in listdir(curdir):
		  return False if isdir(path) else True
	else: return True

def createZeroBlock(filename, path) -> ():
	with open(full_path(filename), "w") as zero:
		zero.write(get_hash(last_block(path)))

def writeBlock(path, zero, name, amount, to_whom, prev_hash = "") -> ():
	files = sort_blocks(path)

	if not files: new_file = "1" + EXTEN_JSON()
	else: new_file = str(files[-1] + 1) + EXTEN_JSON()

	if not prev_hash and len(files) > 0: 
		prev_hash = get_hash(files[-1])

	data = {
		"from": name,
		"amount": amount,
		"to": to_whom,
		"hash": prev_hash,
	}

	with open(full_path(new_file), "w") as block:
		dump(data, block, indent = 4, ensure_ascii = False)

	createZeroBlock(zero, path)

def main() -> ():
	if checkDir(BLOCKCHAIN()): mkdir(BLOCKCHAIN())

	writeBlock(BLOCKCHAIN(), ZERO_BLOCK(), "Alice", 20, "Bob")
	print(checkIntegrity(BLOCKCHAIN(), ZERO_BLOCK()))

if __name__ == "__main__":
	main()
