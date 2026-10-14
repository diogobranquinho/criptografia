# Exemplo de Criptografia em Python

Exemplo simples de criptografia assimétrica com RSA, usando a biblioteca `rsa`.

A ideia é mostrar na prática o funcionamento do par de chaves:

- a **chave pública** cifra a mensagem e pode ser entregue para qualquer pessoa;
- a **chave privada** decifra a mensagem e fica só com o dono.

O que é cifrado com a pública só é decifrado com a privada correspondente.

## Pré-requisitos

- Python 3
- Biblioteca `rsa`

```
pip install rsa
```

## Arquivos

| Arquivo          | O que faz                                           |
|------------------|-----------------------------------------------------|
| `geraChaves.py`  | Gera o par de chaves (pública e privada)            |
| `cifrarMsg.py`   | Cifra uma mensagem usando a chave pública           |
| `decifrarMsg.py` | Decifra a mensagem usando a chave privada           |

## Passo a passo

### 1. Gerar as chaves

```
python3 geraChaves.py
```

```
Tamanho da chave: 2048
Nome do arquivo: my
```

São criados dois arquivos:

- `myPub.txt` — chave pública
- `myPri.txt` — chave privada

### 2. Cifrar uma mensagem

```
python3 cifrarMsg.py
```

```
Nome da chave publica (myPub.txt): myPub.txt
Mensagem a ser cifrada: Ola turma
Nome do arquivo da mensagem (msg.txt): msg.txt
```

O arquivo `msg.txt` fica com o conteúdo cifrado (em binário, não dá para ler).

### 3. Decifrar a mensagem

```
python3 decifrarMsg.py
```

```
Nome da chave privada (myPri.txt): myPri.txt
Nome do arquivo da mensagem (msg.txt): msg.txt
Mensagem decifrada: Ola turma
```

## Exercícios sugeridos

1. Abra o `myPub.txt` e o `myPri.txt` num editor de texto e compare os dois.
2. Tente decifrar a mensagem usando a chave privada de **outro** par de chaves. O que acontece?
3. Cifre a mesma mensagem duas vezes e compare os arquivos gerados. São iguais?
4. Troque chaves públicas com um colega e mande uma mensagem que só ele consiga ler.

## Observações importantes

**Tamanho da mensagem.** O RSA só cifra mensagens menores que a chave. O limite é
o tamanho da chave em bytes menos 11. Exemplos:

| Chave     | Mensagem máxima |
|-----------|-----------------|
| 1024 bits | 117 bytes       |
| 2048 bits | 245 bytes       |

Letras com acento ocupam 2 bytes. Se passar do limite, aparece o erro
`OverflowError`. Na vida real o RSA não é usado para cifrar o texto inteiro:
ele cifra uma chave simétrica (AES, por exemplo), e essa chave cifra a mensagem.

**Tamanho da chave.** Use no mínimo 2048 bits. Chaves de 512 ou 1024 bits servem
só para testar e já são consideradas inseguras.

**Chave privada.** O arquivo `...Pri.txt` é salvo sem senha. Não compartilhe e
não suba para o GitHub.

**Uso didático.** Este exemplo é para estudo. A biblioteca `rsa` é escrita em
Python puro e não é indicada para sistemas reais. Em produção, use bibliotecas
como a `cryptography`.

## Autor

* **Diogo Branquinho Ramos** - [diogobranquinho](https://github.com/diogobranquinho)
