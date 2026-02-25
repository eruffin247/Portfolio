# Secure Password Generator

## Description
The Secure Password Generator is a python program that generates random passwords per request. This program utilizes the **secrets** module to ensure security.  

The **secrets** module is cryptographically unpredidicable as it does not randomly generate a string, but rather have the OS's CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) randomly produce it. The **random** module is a non-secure PRNG (Pseudo-Random Number Generator) that randomly produces a string also, but is reversible. This allows anyone who can discover the *seed*, which is key part of the algorithm used to generate a "random" password, to predict what the output would be.  

With this program, the number of possible passwords that can be produced is $2^{93}$, which equivalates to 9,903,520,314,283,042,199,192,993,792 combinations, or 9.9 octillion for short.
