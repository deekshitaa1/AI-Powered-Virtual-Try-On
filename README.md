# 👗 AI Virtual Try-On (CP-VTON + Streamlit)

This project integrates **CP-VTON** (Cloth Parsing-based Virtual Try-On Network) with a **Streamlit app**.

## 🚀 Setup Instructions

1. Extract this ZIP folder.

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Clone CP-VTON repo and copy required files:
   ```bash
   git clone https://github.com/minar09/cp-vton-plus.git
   cp cp-vton-plus/test.py ./
   cp -r cp-vton-plus/models ./
   cp -r cp-vton-plus/utils ./
   ```

4. Download pretrained weights and place in:
   ```
   checkpoints/cp_vton.pth
   ```

5. Place your **VITON+ dataset** inside:
   ```
   datasets/
   ```

6. Run Streamlit app:
   ```bash
   streamlit run app.py
   ```

7. Upload:
   - A person image
   - A clothing image

   🎉 Get your virtual try-on result!
