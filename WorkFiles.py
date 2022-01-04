
from datetime import datetime


def gravaArquivo(nomeDoArquivo ,txt):
		try:
			arquivo = open(nomeDoArquivo,'w+')
			arquivo.write(txt)
		except Exception:
			print(Exception.with_traceback)
		
		finally:
			arquivo.close()
			
			

def atualizaArquivo(nomeDoArquivo ,txt):
		try:
			arquivo = open(nomeDoArquivo,'a+')
			arquivo.write(txt)
		except Exception:
			print(Exception.with_traceback)
		    
		finally:
			arquivo.close()
			
			
def log (txt):	
  	  data =  datetime.now().strftime('%d/%m/%Y %H:%M')  	  
  	  nomeDoArquivo = "log.txt"
  	  txtLog = data +'\n'
  	  txtlog = +txtLog+txt+'\n\n\n'
  	  atualizaArquivo(nomeDoArquivo,txt)		
  	  
  	  
	
	
def lerArquivo():
	return None
	
	
def retornaListaDeProdutos():
	return None


def test():
	return None





