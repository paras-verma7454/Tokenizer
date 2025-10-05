import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")

text="Hey there! My name is Paras" 
tokens= enc.encode(text)

# Tokens: [25216, 1354, 0, 3673, 1308, 382, 145961]
print("Tokens:", tokens)

decoded = enc.decode(tokens)

# Decoded: Hey there! My name is Paras
print("Decoded:",decoded)