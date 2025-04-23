import torch
import streamlit as st

torch.classes.__path__ = []

st.title("Torch")
st.write(f"{torch.cuda.is_available() = }")

x = torch.rand(5, 3)
st.write(x)
