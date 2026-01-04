# 0/1 Knapsack Dynamic Programming
# Kasus: Optimasi Isi Tas Mahasiswa Informatika

def knapsack_dp(items, capacity_kg, scale=10):
    """
    items: list of dict {name, w (kg), v}
    capacity_kg: float (kg)
    scale: int (untuk mengubah kg desimal -> integer)
    """
    # ubah ke integer agar DP mudah
    W = int(round(capacity_kg * scale))
    weights = [int(round(it["w"] * scale)) for it in items]
    values = [it["v"] for it in items]
    n = len(items)

    # dp[i][w] = nilai max pakai item 0..i-1 dengan kapasitas w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wi = weights[i - 1]
        vi = values[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]  # tidak ambil
            if wi <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)  # ambil

    # rekonstruksi item terpilih
    selected = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= weights[i - 1]

    selected.reverse()
    total_weight = sum(it["w"] for it in selected)
    total_value = sum(it["v"] for it in selected)

    return total_value, total_weight, selected


if __name__ == "__main__":
    # DATA 10 ITEM (Informatika) - tanpa payung/buku referensi/kotak makan
    items = [
        {"name": "Laptop",               "w": 2.0, "v": 95},
        {"name": "Charger Laptop",       "w": 0.5, "v": 40},
        {"name": "Powerbank",            "w": 0.4, "v": 32},
        {"name": "Headset/Earphone",     "w": 0.2, "v": 22},
        {"name": "Mouse Wireless",       "w": 0.2, "v": 20},
        {"name": "Flashdisk/SSD Eksternal","w": 0.3,"v": 30},
        {"name": "Kabel LAN/USB Hub",    "w": 0.3, "v": 24},
        {"name": "Notebook kecil",       "w": 0.4, "v": 18},
        {"name": "Modem/MiFi",           "w": 0.4, "v": 28},
        {"name": "Keyboard Portable",    "w": 0.6, "v": 26},
    ]

    capacity = 7.0  # kg (kasus utama)
    max_value, total_weight, selected_items = knapsack_dp(items, capacity)

    print("=== HASIL 0/1 KNAPSACK (DYNAMIC PROGRAMMING) ===")
    print(f"Kapasitas Tas : {capacity} kg")
    print(f"Nilai Maksimum: {max_value}")
    print(f"Total Berat   : {total_weight:.1f} kg")
    print("\nItem Terpilih:")
    for i, it in enumerate(selected_items, 1):
        print(f"{i}. {it['name']} (w={it['w']} kg, v={it['v']})")
