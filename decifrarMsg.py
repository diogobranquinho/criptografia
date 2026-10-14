#python3 version
import rsa
print('\\-------------------------------//')
print('**Prj Banco de Dados Distribuidos**')
print('\\-------------------------------//')
print('Decifrador de mensagens')
print('Digite as seguintes informacoes')
arqnomepri = input('Nome da chave privada (myPri.txt): ')
arqnomemsg = input('Nome do arquivo da mensagem (msg.txt): ')

##abro o arquivo com a chave
arq = open(arqnomepri,'rb')
##carrego a chave
txt = arq.read()
arq.close()

#decodifico para o formato expoente e modulo
pri = rsa.PrivateKey.load_pkcs1(txt, format='PEM')

#abro o arquivo com a msg
arq = open(arqnomemsg,'rb')

##carrego a msg cifrada
msgc = arq.read()
arq.close()

#decifro a msg
msg = rsa.decrypt(msgc,pri)

print('Mensagem decifrada: ' + msg.decode('utf-8'))



