import os
import re

def organizar_arquivos_por_data(diretorio):
    cont = 0
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            teste = re.match(r'^lucasgf-(20[0-2]\d{1})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])-', file)
            if teste is None:
                print('Sim', teste)
                regex_data = r'(20[0-2]\d{1})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])'
                match = re.search(regex_data, file)
                if match:
                    formato = file.split('.')[-1]
                    origem = os.path.join(root, file)
                    codigo = 'lucasgf-'+str(match.group()) +'-'+ str(cont) + '.' + formato

                    destino = os.path.join(root, codigo)
                    os.rename(origem,destino)
                    cont += 1
                else:
                    regex_data = r'(20[0-2]\d{1})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])'
                    match = re.search(regex_data, file)
                    if match:
                        formato = file.split('.')[-1]
                        origem = os.path.join(root, file)
                        codigo = 'lucasgf-'+str(match.group()) +'-'+ str(cont) + '.' + formato

                        destino = os.path.join(root, codigo)
                        os.rename(origem,destino)
                        cont += 1

            print(file, teste)
    print(cont)

organizar_arquivos_por_data('/mnt/2244D41D44D3F211/lucas/stage/2024')
