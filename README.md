## Tokenizer

```url
https://tokenizer-inws.onrender.com/My fav anime is One piece
```
## What is Tokenization?

**Tokenization** is the process of converting text into smaller units called *tokens* (such as words, subwords, or characters) which are then mapped to unique numerical IDs so that machine learning models can understand and process them.

- It is **case-sensitive**, meaning `"anime"` and `"Anime"` are assigned different tokens.

## Example

```json
{
  "Tokens": "[5444, 11726, 35868, 382, 5108, 9047]",
  "Decoded": "My fav anime is One piece"
}
```
<br/>

```json
{
  "Tokens": "[5444, 11726, 80118, 382, 5108, 9047]",
  "Decoded": "My fav Anime is One piece"
}
```


**Note:**  
- Only the word `"anime"` vs `"Anime"` produces a different token ID: `35868` vs `80118`.
- All other tokens remain the same.

## Summary

Tokenization enables text to be processed as numbers for machine learning, with each unique word, casing, or symbol resulting in different token IDs.
