import pyperclip, sys, random
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def main():
 myMessage =input("Enter your message to encrypt or decrypt - ") 
 myKey = getRandomKey() #RandomKey gives random key for encryption or decryption
 myMode = input('Do you want to encrypt or decrypt? ') #Type encrypt or decrypt
 checkValidKey(myKey)
 if myMode == 'encrypt':
  translated = encryptMessage(myKey, myMessage)
  print('Using key %s' % (myKey))
 elif myMode == 'decrypt':
  key= input('Enter key to decrypt - ')
  translated = decryptMessage(key, myMessage)
 print('The %sed message is:' % (myMode))
 print(translated)
 pyperclip.copy(translated)
 print()
 print('This message has been copied to the clipboard.')

def checkValidKey(key):
 keyList = list(key)
 lettersList = list(LETTERS)
 keyList.sort()
 lettersList.sort()
 if keyList != lettersList:
  sys.exit('There is an error in the key or symbol set.')

def encryptMessage(key, message):
 return translateMessage(key, message, 'encrypt')
def decryptMessage(key, message):
 return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
 translated = ''
 charsA = LETTERS
 charsB = key
 if mode == 'decrypt':
 # For decrypting, we can use the same code as encrypting. We
 # just need to swap where the key and LETTERS strings are used.
  charsA, charsB = charsB, charsA

 # loop through each symbol in the message
 for symbol in message:
  if symbol.upper() in charsA:
 # encrypt/decrypt the symbol
   symIndex = charsA.find(symbol.upper())
   if symbol.isupper():
    translated += charsB[symIndex].upper()
   else:
    translated += charsB[symIndex].lower()
  else:
   translated += symbol
 return translated

def getRandomKey():
  key = list(LETTERS)
  random.shuffle(key)
  return ''.join(key)
if __name__ == '__main__':
 main()
