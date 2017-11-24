Hostname = "local"

Command_MAIN = {"Cryptography" :("1","cd 1","cd Cryptography",":d Cryptography",":d 1"    ),
				"Scanners"     :("2","cd 2","cd Scanners",":d Scanners",":d 2"            ),
			 	"Bots"         :("3","cd 3","cd Bots",":d Bots",":d 3"                    ),
			 	"BruteForce"   :("4","cd 4","cd BruteForce",":d BruteForce",":d 4"        ),
			 	"Malware"      :("5","cd 5","cd Malware",":d Malware",":d 5"              ),
			 	"Steganography":("6","cd 6","cd Steganography",":d Steganography",":d 6"  ),
			 	"Components"   :("0","./0","./COMPONENTS.571",":f COMPONENTS.571",":f 0"  )}

Command_CRPT = {"Caesar" 	   :("1","./1","./CAESAR.571",":f CAESAR.571",":f 1"  	      ),
				"Vishener"     :("2","./2","./VISHENER.571",":f VISHENER.571",":f 2"	  ),
				"Replace"      :("3","./3","./REPLACE.571",":f REPLACE.571",":f 3"	      ),
				"Homophonic"   :("4","./4","./HOMOPHONIC.571",":f HOMOPHONIC.571",":f 4"  ),
				"RSA"		   :("5","./5","./RSA.571",":f RSA.571",":f 5"			      ),
				"AES"		   :("6","./6","./AES.571",":f AES.571",":f 6"			      ),
				"XOR"          :("7","./7","./XOR.571",":f XOR.571",":f 7"                ),
				"Cryptanalysis":("0","./0","./CRYPTANALYSIS.571","./CRYPTANALYSIS",":f 0" )}

Command_BOTS = {"Parser"       :("1","./1","./PARSER.571",":f PARSER.571",":f 1"          ),
				"Clicker"      :("2","./2","./CLICKER.571",":f CLICKER.571",":f 2"        ),
				"TorScript"    :("3","./3","./TORSCRIPT.571",":f TORSCRIPT.571",":f 3"    )}

Command_BRTF = {"SSH"          :("1","./1","./SSH.571",":f SSH.571",":f 1"                ),
				"Caesar"       :("2","./2","./CAESAR.571",":f CAESAR.571",":f 2"          ),
				"RockYou"      :("0","./0","./ROCKYOU.TXT",":f ROCKYOU.571",":f 0"        )}

Command_MLWR = {"Locker"       :("1","./1","./LOCKER.571",":f LOCKER.571",":f 1"          ),
				"Crypter"      :("2","./2","./CRYPTER.571",":f CRYPTER.571",":f 2"        ),
				"Cryptlocker"  :("3","./3","./CRYPTLOCKER.571",":f CRYPTLOCKER.571",":f 3"),
				"Py-virus"     :("4","./4","./PYVIRUS.571",":f PYVIRUS.571",":f 4"        )}

Command_SCAN = {"Scanner"      :("1","./1","./SCANNER.571",":f SCANNER.571",":f 1"        )}

Command_STGN = {"Zip"          :("1","./1","./ZIP.571",":f ZIP.571",":f 1"                ),
				"Message"      :("2","./2","./MESSAGE.571",":f MESSAGE.571",":f 2"        ),
				"Read-bytes"   :("0","./0","./READ_BYTES.571",":f READ_BYTES.571",":f 0"  )}

Command_ADDT = {"Clear"        :("&", "clear", "wash", ":c"                               ),
				"Info"         :("!", "info", ":i"                                        ),
				"Help"         :("?", "help", ":h"                                        ),
				"Check"        :("/", "ls", "dir", ":l"                                   ),
				"Back"         :("<", "cd ..", "cd", "cd ", "back", ":b"                  ),
				"Exit"         :("$", "exit", "quit", ":q"                                )}