# Secure Password Generator

## Description
The Secure Password Generator is a python program that generates random passwords per request. This program utilizes the **secrets** module to ensure security.  

The **secrets** module is cryptographically unpredidicable as it does not randomly generate a string, but rather have the OS's CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) randomly produce it. The **random** module is a non-secure PRNG (Pseudo-Random Number Generator) that randomly produces a string also, but is reversible. This allows anyone who can discover the seed 
