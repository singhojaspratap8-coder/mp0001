#!/usr/bin/env python3
import sys
import base64

def main():
    print("==================================================")
    print("      MP0001 - Personal Text Encoder/Decoder      ")
    print("            Created By: Ojas Pratap Singh         ")
    print("==================================================")
    print("Purpose: Hide your personal text securely using   ")
    print("         Base64 encoding and decoding.            ")
    print("==================================================")
    
    if len(sys.argv) < 3:
        print("\n[!] Usage Guide:")
        print("    To Encode: mp0001 -e \"Your secret text\"")
        print("    To Decode: mp0001 -d \"Encoded_string\"\n")
        return

    mode = sys.argv[1]
    text = " ".join(sys.argv[2:])

    if mode == "-e":
        encoded_bytes = base64.b64encode(text.encode("utf-8"))
        encoded_text = encoded_bytes.decode("utf-8")
        print(f"\n[+] Encrypted Text:\n    {encoded_text}\n")
        
    elif mode == " -d" or mode == "-d":
        try:
            decoded_bytes = base64.b64decode(text.encode("utf-8"))
            decoded_text = decoded_bytes.decode("utf-8")
            print(f"\n[+] Decrypted Text:\n    {decoded_text}\n")
        except Exception:
            print("\n[!] Error: Invalid encoded string provided!\n")
            
    print("==================================================")
    print("          Powered by Ojas Pratap Singh            ")
    print("==================================================")

if __name__ == "__main__":
    main()
