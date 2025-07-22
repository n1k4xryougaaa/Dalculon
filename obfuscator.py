# ver test
# obfuscator.py
import os
import marshal
import zlib
import base64
import hashlib
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    logo = r"""
     ____        _            _             
    |  _ \  __ _| | ___ _   _| | ___  _ __  
    | | | |/ _` | |/ __| | | | |/ _ \| '_ \ 
    | |_| | (_| | | (__| |_| | | (_) | | | |
    |____/ \__,_|_|\___|\__,_|_|\___/|_| |_|
    """
    description = "🔐 Multi‐layer Python Obfuscator (marshal • zlib • base64 • SHA256)"
    print(logo)
    print(description)
    print()

def obfuscate_payload(source_code: str, file_name: str) -> bytes:
    code_obj    = compile(source_code, file_name, 'exec')
    marshalled  = marshal.dumps(code_obj)
    compressed  = zlib.compress(marshalled, level=9)
    return compressed

def generate_stub(encoded_payload: str, sha256_hash: str) -> str:
    # Stub loader dengan flow: clear → verify → decode → exec, dibungkus dalam if/main + try/except
    return f"""import os, base64, zlib, marshal, hashlib, sys

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    clear_screen()
    # Load payload
    payload = base64.b64decode("{encoded_payload}")
    # Verifikasi SHA256
    if hashlib.sha256(payload).hexdigest() != "{sha256_hash}":
        raise ValueError("hash mismatch! File mungkin telah dimodifikasi.")
    # Decode & exec
    code = marshal.loads(zlib.decompress(payload))
    exec(code)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(f"Error: {{e}}")
"""

def multi_layer_obfuscate(source_path: str, output_path: str, layer_count: int):
    with open(source_path, 'r', encoding='utf-8') as f:
        source = f.read()

    current_code = source
    clear_screen()
    print_logo()
    print(f"Mulai obfuscate: {layer_count} lapis")

    for i in range(layer_count):
        percent = int(((i+1) / layer_count) * 100)
        sys.stdout.write(f"\rProgress: {percent}% (lapis {i+1}/{layer_count})")
        sys.stdout.flush()

        obf_bytes = obfuscate_payload(current_code, source_path)
        encoded   = base64.b64encode(obf_bytes).decode('utf-8')
        sha256    = hashlib.sha256(obf_bytes).hexdigest()
        current_code = generate_stub(encoded, sha256)
        time.sleep(0.01)

    sys.stdout.write("\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(current_code)

    print(f"\n[✔] File berhasil di-obfuscate sebanyak {layer_count} lapis.")
    print(f"[➜] Hasil disimpan di: {output_path}")

if __name__ == "__main__":
    clear_screen()
    print_logo()

    input_path  = input("  > Path file input  : ").strip()
    output_path = input("  > Path file output : ").strip()

    try:
        layer = int(input("  > Jumlah lapisan obfuscate: ").strip())
    except ValueError:
        print("❌ Jumlah lapisan harus berupa angka.")
        sys.exit(1)

    if not os.path.isfile(input_path):
        print(f"❌ File '{input_path}' tidak ditemukan.")
        sys.exit(1)

    multi_layer_obfuscate(input_path, output_path, layer)
