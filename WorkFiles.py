from datetime import datetime
import enum

def gravaArquivo(nomeDoArquivo, txt, tipo):
    try:
        arquivo = open(nomeDoArquivo, tipo.value)
        arquivo.write(txt)
    except Exception:
        print(Exception.with_traceback)

    finally:
        arquivo.close()





class FileOption(enum.Enum):
    RECORD= 'w+'
    UPDATE = 'a+'
    




def log(txt):
    data = datetime.now().strftime('%d/%m/%Y %H:%M')
    nomeDoArquivo = "log.txt"
    txtLog = data + '\n'
    txtLog = +txtLog + txt + '\n\n\n'
    atualizaArquivo(nomeDoArquivo, txtLog)


def lerArquivo():
    return None
