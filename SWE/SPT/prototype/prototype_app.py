# ===Imports===
import streamlit as st
from passgen import gen_password

st.title("🚨 Prototype SPT  🔒")

# ===Intro===
st.write("""
## Introduction 🎬
This tool to for generating cryptographically secure random passwords.

## How to Use 📑
1. Select the number of passwords you would like to generate.
2. Select the desired length of the password.
3. Click the "Generate Password" button.
""")

# ===Generate Password===
st.write("## Generate Your Password 🤐")

num_of_passwords = st.radio(
    "How many passwords would you like to generate?",
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

pass_length = st.radio(
"Length of password?",
[12, 13, 14, 15, 16, 17, 18, 19, 20]
)

if st.button("Generate Password"):
    if num_of_passwords == 1:
        st.write("Here is your password! ⬇️")
    else:
        st.write(f"Here are your {num_of_passwords} passwords! ⬇️")

    for i in range(num_of_passwords):
        password = gen_password(pass_length)
        st.write(f"Password {i + 1}: {password}")