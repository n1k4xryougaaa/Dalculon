# 🔐 Dalculon - Multi-Layer Python Obfuscator

Dalculon is a **multi-layer obfuscator** for Python that protects your source code using a combination of:
- `marshal`
- `zlib`
- `base64`
- `hashlib` (SHA-256 integrity verification)

Each layer wraps the previous code in a new encoding, producing a single `.py` file that's still executable but very hard to read or reverse‑engineer.

---

## 🧠 Key Features

- **Configurable layers**: specify how many obfuscation layers you want  
- **SHA-256 integrity**: each layer self‑verifies before execution  
- **Pure Python output**: results in a `.py` file (no `.pyc` or binaries)  
- **Runtime checker**: aborts if any payload is tampered  
- **Cross‑platform**: works on Termux (Android), Linux, and Windows  

---

## 📦 How It Works

For each layer:
1. **Compile** your source → `marshal.dumps()`  
2. **Compress** the bytecode → `zlib.compress()`  
3. **Encode** → `base64.b64encode()`  
4. **Hash** → `hashlib.sha256()`  
5. **Wrap** in a stub loader that clears screen and `exec()`

The process repeats _n_ times (as you choose). At runtime, each stub reverses its layer in reverse order until the original code runs.

---

## 🛠 Installation & Usage

### Termux / Android
```bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip

git clone https://github.com/n1k4xryougaaa/Dalculon
cd Dalculon
python obfuscator.py
```

### Linux (Debian/Ubuntu/Arch/etc.)
```
sudo apt update && sudo apt install python3 git -y
git clone https://github.com/n1k4xryougaaa/Dalculon
cd Dalculon
python3 obfuscator.py
```

---

### Windows
Install Python from python.org

Open Command Prompt:
```
git clone https://github.com/n1k4xryougaaa/Dalculon
cd Dalculon
python obfuscator.py
```

▶️ Example
Once you run ```obfuscator.py```, you will be prompted:
```
  > Path to input file  : my_script.py
  > Path to output file : obf_my_script.py
  > Number of layers    : 10
```

After completion, ```obf_my_script.py``` contains your code obfuscated 10 times. To execute it, simply run:
```
python obf_my_script.py
```

---

⚠️ Notes
Do not modify the generated file, or the ```SHA-256``` check will fail.

Higher layer counts increase file size and runtime overhead. Use responsibly.

The script is designed to be extended: you can add ```XOR/AES``` layers or other transforms.

📁 Repository Structure
```
Dalculon/
├── obfuscator.py     # Main obfuscation script
└── README.md         # This documentation file
```

👤 Author
Ryougaa Hidekii
GitHub: @n1k4xryougaaa

---

📜 License
This project is licensed under the MIT License.
