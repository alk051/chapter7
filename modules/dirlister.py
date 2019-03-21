print ("#Esse comando lista arquivos do diretorio corrente e retorna a lista em forma de string ")

import os
def run(**args):

	print "[*] In dirlister module."
	files = os.listdir(".")

	return str(files)

