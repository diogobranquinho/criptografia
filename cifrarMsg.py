import rsa
print ' \\-------------------------------//'
print ' **Prj Banco de Dados Distribuidos**'
print ' \\-------------------------------//'
print 'Cifrador de mensagens'
print 'Digite as seguintes informacoes'
arqnomepub = raw_input('Endereco da chave publica (c:\chaves\myPub.txt): ')
msg = raw_input('Mensagem a ser cifrada: ')
arqnomemsg = raw_input('Endereco e nome da mensagem (c:\msg.txt): ')

##abro o arquivo com a chave
arq = open(arqnomepub,'r')
##carrego a chave
txt = ''
for linha in arq:
   txt = txt + linha
arq.close()

#decodifico para o formato expoente e modulo
pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')

#cifro a msg
msgc = rsa.encrypt(msg,pub)

#salvo a msgc no arquvio
arq = open(arqnomemsg,'w')
arq.write(msgc)
arq.close()

print 'Mensagem cifrada no arquivo ' + arqnomemsg



