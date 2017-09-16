import rsa
print ' \\-------------------------------//'
print ' **Prj Banco de Dados Distribuidos**'
print ' \\-------------------------------//'
print 'Decifrador de mensagens'
print 'Digite as seguintes informacoes'
arqnomepri = raw_input('Endereco da chave privada (c:\chaves\myPri.txt): ')
arqnomemsg = raw_input('Endereco e nome da mensagem a ser decifrada (c:\msg.txt): ')

##abro o arquivo com a chave
arq = open(arqnomepri,'r')
##carrego a chave
txt = ''
for linha in arq:
   txt = txt + linha
arq.close()

#decodifico para o formato expoente e modulo
pri = rsa.PrivateKey.load_pkcs1(txt, format='PEM')

#abro o arquivo com a msg
arq = open(arqnomemsg,'r')
##carrego a msg cifrada
msgc = ''
for linha in arq:
   msgc = msgc + linha
arq.close()

#decifro a msg
msg = rsa.decrypt(msgc,pri)

print 'Mensagem decifrada: ' + msg



