import argparse
from vigenere import vigenere_decrypt, vigenere_encrypt
from modes import ecb_decrypt, ecb_encrypt, cbc_decrypt, cbc_encrypt
parser = argparse.ArgumentParser(description="Encryption/Decryption")

parser.add_argument(
    "-e",
    action="store_true",
)

parser.add_argument(
    "-d",
    action="store_true",
)
parser.add_argument(
    "-key",
    required=True,
)

parser.add_argument(
    "cipher",
    choices=["AES","vigenere"]
)
parser.add_argument(
    "mode",
    nargs="?",
)
parser.add_argument(
    "input",
)
parser.add_argument(
    "-f",
    action="store_true"
)
parser.add_argument(
    "output",
    nargs="?",
)
parser.add_argument(
    "-iv",
)

args = parser.parse_args()
if args.f==False and args.output==None:  
    if args.cipher=="vigenere":
        if args.e==True and args.d==False:
            re=vigenere_encrypt(args.input,args.key)
            print(re)
        elif args.d==True and args.e==False:
            ra=vigenere_decrypt(args.input,args.key)
            print(ra)
        elif args.e==False and args.d==False:
            print("Please enter either encrypt or decrypt ")
        else:
            print("Please enter either -e or -d")

    if args.cipher=="AES":
        if args.mode=="ECB" and args.iv==None:
            if args.e==True and args.d==False:
                a=[ord(x) for x in args.input]
                b=ecb_encrypt(a,args.key)
                print(b)    
            elif args.d==True and args.e==False:
                c=ecb_decrypt(args.input,args.key)
                for x in c:
                    print(chr(x),end="")
            elif args.e==False and args.d==False:
                print("Please enter either encrypt or decrypt ")
            else:
                print("Please enter either -e or -d")
        elif args.mode=="CBC":
            if args.e==True and args.d==False and args.iv==None:
                a=[ord(x) for x in args.input]
                b=cbc_encrypt(a,args.key)
                print("Initialisation Vector:",b[0])
                print("Ciphertext:",b[1])
            elif args.d==True and args.e==False and args.iv!=None:
                c=cbc_decrypt(args.input,args.key,args.iv)
                for x in c:
                    print(chr(x),end="")
            else:
                print("enter command properly")
        else:
            print("Enter command properly")
elif args.f==True and args.output!=None:
    if args.cipher == "vigenere":
        if args.e and not args.d:
            with open(args.input, "r") as file:
                plaintext = file.read()
        
            ciphertext = vigenere_encrypt(plaintext, args.key)
        
            with open(args.output, "w") as file:
                file.write(ciphertext)

        elif args.d and not args.e:
            with open(args.input, "r") as file:
                ciphertext = file.read()
        
            plaintext = vigenere_decrypt(ciphertext, args.key)
        
            with open(args.output, "w") as file:
                file.write(plaintext)

        elif not args.e and not args.d:
            print("Please enter either encrypt or decrypt")
        
        else:
            print("Please enter either -e or -d")
    elif args.cipher == "AES":

        if args.mode == "ECB" and args.iv is None:

            if args.e and not args.d:
                with open(args.input, "rb") as file:
                    plaintext = list(file.read())
                
                ciphertext = ecb_encrypt(plaintext, args.key)
                
                with open(args.output, "w") as file:
                    file.write(ciphertext)


            elif args.d and not args.e:
                with open(args.input, "r") as file:
                    ciphertext = file.read()
                
                plaintext = ecb_decrypt(ciphertext, args.key)
                
                with open(args.output, "wb") as file:
                    file.write(bytes(plaintext))

            elif not args.e and not args.d:
                print("Please enter either encrypt or decrypt")
                
            else:
                print("Please enter either -e or -d")


        elif args.mode == "CBC":

            if args.e and not args.d and args.iv is None:
                with open(args.input, "rb") as file:
                    plaintext = list(file.read())
                
                iv, ciphertext = cbc_encrypt(plaintext, args.key)
                
                with open(args.output, "w") as file:
                    file.write(ciphertext)
                    
                print("Initialisation Vector:", iv)


            elif args.d and not args.e and args.iv is not None:
                with open(args.input, "r") as file:
                    ciphertext = file.read()
                
                plaintext = cbc_decrypt(ciphertext, args.key, args.iv)
                
                with open(args.output, "wb") as file:
                    file.write(bytes(plaintext))

            elif not args.e and not args.d:
                print("Please enter either encrypt or decrypt")
                
            else:
                print("Enter command properly")
                
        else:
            print("Enter command properly")
        
else:
    print("Enter command properly")
