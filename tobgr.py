import colorsys

# tobgr.py
# Python 3.11.9
# Fungsi untuk convert berbagai format warna menjadi BGR

# Helper untuk clamp nilai 0-255
def clamp(val, min_val=0, max_val=255):
    return max(min_val, min(max_val, val))

# Convert HEX ke RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    m = int(hex_color[4:6], 16)
    return (r, g, m)

# Convert HSL ke RGB (0-360, 0-100, 0-100)
def hsl_to_rgb(h, s, l):
    h = h / 360
    s = s / 100
    l = l / 100
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (int(r * 255), int(g * 255), int(b * 255))

# Convert HSV ke RGB (0-360, 0-100, 0-100)
def hsv_to_rgb(h, s, v):
    h = h / 360
    s = s / 100
    v = v / 100
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (int(r * 255), int(g * 255), int(b * 255))

# Convert umum ke BGR
def convert_to_bgr(value, mode="rgb"):
    mode = mode.lower()

    if mode == "rgb":
        r, g, b = value
    elif mode == "hex":
        r, g, b = hex_to_rgb(value)
    elif mode == "hsl":
        r, g, b = hsl_to_rgb(*value)
    elif mode == "hsv":
        r, g, b = hsv_to_rgb(*value)
    else:
        raise ValueError("Mode warna tidak dikenal. Gunakan rgb, hex, hsl, atau hsv.")

    return (b, g, r)

if __name__ == "__main__":
    print("=== TO-BGR Converter ===")
    print("Pilih mode input warna:")
    print("1. RGB")
    print("2. HEX")
    print("3. HSL")
    print("4. HSV")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        r = int(input("R: "))
        g = int(input("G: "))
        b = int(input("B: "))
        print("BGR:", convert_to_bgr((r, g, b), "rgb"))

    elif pilihan == "2":
        hex_color = input("HEX (#RRGGBB): ")
        print("BGR:", convert_to_bgr(hex_color, "hex"))

    elif pilihan == "3":
        h = float(input("H (0-360): "))
        s = float(input("S (0-100): "))
        l = float(input("L (0-100): "))
        print("BGR:", convert_to_bgr((h, s, l), "hsl"))

    elif pilihan == "4":
        h = float(input("H (0-360): "))
        s = float(input("S (0-100): "))
        v = float(input("V (0-100): "))
        print("BGR:", convert_to_bgr((h, s, v), "hsv"))

    else:
        print("Pilihan tidak valid.")
