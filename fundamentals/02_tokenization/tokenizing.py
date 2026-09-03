import tiktoken

"""
A token might contain:

A whole word
Part of a word
A space + a word
Punctuation
A piece of a word

"""

MODEL = "gpt-4.1-mini"
TEXT = "Hi my name is rock"


encoding = tiktoken.encoding_for_model(MODEL)

tokens = encoding.encode(TEXT)

print(f"Original text: {TEXT}")
print(f"Token IDs: {tokens}")
print(f"Number of tokens: {len(tokens)}")

print("\nIndividual tokens:")

for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id}: {token_text!r}")  #!r to reveal the spaces


