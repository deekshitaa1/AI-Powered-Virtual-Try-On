import streamlit as st
from subprocess import run
from PIL import Image
import os

st.set_page_config(page_title="AI Virtual Try-On", page_icon="👗")

st.title("👗 AI-Powered Virtual Try-On (CP-VTON)")

person = st.file_uploader("Upload your photo", type=["jpg","jpeg","png"])
clothes = st.file_uploader("Upload garment image", type=["jpg","jpeg","png"])

if st.button("Generate Try-On") and person and clothes:
    os.makedirs("data", exist_ok=True)
    with open("data/person.jpg", "wb") as f:
        f.write(person.read())
    with open("data/clothes.jpg", "wb") as f:
        f.write(clothes.read())

    # Call CP-VTON test.py
    exit_code = run([
        "python", "test.py",
        "--checkpoint", "checkpoints/cp_vton.pth",
        "--person", "data/person.jpg",
        "--clothes", "data/clothes.jpg",
        "--output_dir", "results/"
    ])

    result_path = "results/tryon.png"
    if os.path.exists(result_path):
        result = Image.open(result_path)
        st.image(result, caption="✨ Virtual Try-On Result ✨")
    else:
        st.error("⚠️ Inference failed. Check test.py and arguments.")
