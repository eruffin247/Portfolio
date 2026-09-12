# ===Imports===
import streamlit as st
from passgen import gen_password

st.title("🚨 Prototype SPT  🔒")

# ===Intro===
st.write("""
## Introduction 🎬
This tool to for generating cryptographically secure random passwords.

## How to Use 📑
1. Select the desired length of the password
2. Click the "Generate Password" button
""")

# ===Generate Password===
st.write("## Generate Your Password")
pass_length = st.radio(
"Length of password?",
[12, 13, 14, 15, 16, 17, 18, 19, 20]
)

if st.button("Generate Password"):
    password = gen_password(pass_length)
    st.write(f"Password: {password}")