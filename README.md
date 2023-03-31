
# ObsiEnc

From `Obsidian` and `Encrypt`... so damn complex, I know.

---

## What is this?

This tool provides a complicated (and boring) way of backing up our vaults. The idea is to use *GitHub* as our cloud, but the problem is that files are stored as plain text (markdown). If anyone gains access to our *GitHub Vault*, they would have access to everything and could read all our notes without any problem. That's where **ObsiEnc** comes in to save our super confidential notes. Instead of storing plain text, we store encrypted files. That's it. Thanks for watching... [plays epic outro]

## Wanna know more?

Sure, we use AES (Advance Encryption Standard) that's just the most widely used encryption algorithm... and Python, we all know Python, right? That's it, please don't ask me more questions because I don't know the answer. 

## Advantages

-  **Privacy** (?) : Just in the case that someone access your private repository.

## Disadvantages

-  **CORRUPTION**: There is the possibility that your files get corrupted, either by the process of encryption by itself or by editing files when they are already encrypted... just changing one of those gibberish characters and your file may be ruined. 
-  **Complete lost**: If you forget your *Passphrase* your files is bye bye, so be careful.
-  **Tedious**: The entire process of setting this up is tedious as F.
-  **Complex**: No 'complex-good', 'complex-unnecessary'.
-  **Boring**: I would have loved to make a plugin that is more user-friendly for everyone, but as I progressed on this project, it seemed more and more unnecessary to me. As a result, I ended up taking the easiest path, at least for me, although for the end user it may be more convoluted... sorry for that.

---

## Are you still here? Okay! Lets set up this BAD boy


Let's do it fast.

### 1. We need four variables:

| Variable name | Description |
| --- | --- |
|  PSWD | Your super secure **Passphrase** |
| ENC_PATH | Directory where your encrypted files are going to be stored |
| DEC_PATH | Directory where your decrypted files are going to be stored |
| salt | Your 32 bytes of *Salt* |

The first three variables can be edited inside the `.env` file, while the last one has to be edited inside the `variables.py` file. To do so, you first have to generate 32 random bytes. You can run `updateSalt.py` to generate the bytes, and then copy the output into `variables.py`.

For your **passphrase** be sure to select something robust, you can use something like [this](https://it-tools.tech/bip39-generator) or another generator.

Three things, before we continue:

  1. Both *PATHS* needs to be a full paths. For example: `/home/user/Documents/YOUR_VAULT`
  2.  Whatever your decryption path is, it **must** end in `Obsidian` (yeah, I know, what a good programmer I am). For example, if your path is `/home/user/Documents/YOUR_VAULT`, your variable should look something like this: `/home/user/Documents/YOUR_VAULT/Obsidian`. Therefore, I recommend creating an `Obsidian` folder inside `Documents` and pasting your entire vault there. That way, you ensure that your files are still safe if anything happens because, as we say, `one never knows` (Latin joke there).
  3.  The same thing as above applies to the encryption path, although in this case, it **must** end in `EncryptRepo`. (Yeap! Programmer of the year over here.)


 ### 2. Run the script with one of this parameters:

-  `enc`: to encrypt
-  `dec`: to decrypt

  For example:

  ```bash
  python Obsienc.py enc
  ```

  That's it. ~The only straightforward step~

# Conclusion

**You shouldn't be using this tool without another backup of your notes, or at least be aware of the potential risks involved**.

Obviously, there are many things that could be improved, so I may revisit this in the future, I don't know, *amanecerá y veremos*.

#### Feel free to edit, delete or just make fun of any part of this code.

