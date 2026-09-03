# Tokenization

This module explores how text is converted into tokens before being processed by a Large Language Model.

## What I Learned

- LLMs do not directly process text as humans do.
- Text is converted into numerical tokens.
- A tokenizer converts text into token IDs using `encode()`.
- Token IDs can be converted back into text using `decode()`.
- Tokens are not always equivalent to words.

## Code

`tokenizing.py` demonstrates:

1. Selecting the tokenizer associated with a model.
2. Encoding text into token IDs.
3. Counting tokens.
4. Decoding individual tokens back into text.

## Technology

- Python
- tiktoken