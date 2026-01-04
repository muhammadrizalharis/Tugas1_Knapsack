import pandas as pd
import time
import matplotlib.pyplot as plt

# ==============================
# KONFIGURASI
# ==============================
DATASET_PATH = r"D:\DATA_RIZAL\KAMPUS\SEMESTER_5\DESAIN_DAN_ANALISIS_ALGORITMA\dataset_knapsack_tas_mahasiswa_informatika.csv"

OUTPUT_TABLE = r"D:\DATA_RIZAL\KAMPUS\SEMESTER_5\DESAIN_DAN_ANALISIS_ALGORITMA\tabel_perbandingan_bruteforce_vs_backtracking_ms.csv"
OUTPUT_GRAPH_TIME = r"D:\DATA_RIZAL\KAMPUS\SEMESTER_5\DESAIN_DAN_ANALISIS_ALGORITMA\grafik_waktu_ms_bruteforce_vs_backtracking.png"
OUTPUT_GRAPH_NODE = r"D:\DATA_RIZAL\KAMPUS\SEMESTER_5\DESAIN_DAN_ANALISIS_ALGORITMA\grafik_node_bruteforce_vs_backtracking.png"

CAPACITY = 7.0

# ==============================
# LOAD DATASET
# ==============================
df = pd.read_csv(DATASET_PATH)

items = []
for _, r in df.iterrows():
    items.append({
        "w": float(r["Weight_kg"]),
        "v": int(r["Value"])
    })

# ==============================
# BRUTE FORCE
# ==============================
def brute_force(items, capacity):
    n = len(items)
    checked = 0
    best = 0

    for mask in range(1 << n):
        checked += 1
        w, v = 0.0, 0
        for i in range(n):
            if mask & (1 << i):
                w += items[i]["w"]
                v += items[i]["v"]
        if w <= capacity and v > best:
            best = v

    return checked, best

# ==============================
# BACKTRACKING (pruning overweight)
# ==============================
def backtracking(items, capacity):
    n = len(items)
    visited = 0
    best = 0

    def dfs(i, w, v):
        nonlocal visited, best
        visited += 1
        if w > capacity:
            return
        if v > best:
            best = v
        if i == n:
            return
        dfs(i + 1, w + items[i]["w"], v + items[i]["v"])
        dfs(i + 1, w, v)

    dfs(0, 0.0, 0)
    return visited, best

# ==============================
# EKSPERIMEN
# ==============================
rows = []

for n in range(4, len(items) + 1):
    subset = items[:n]

    t0 = time.perf_counter()
    brute_checked, best_val = brute_force(subset, CAPACITY)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    back_nodes, _ = backtracking(subset, CAPACITY)
    t3 = time.perf_counter()

    # Ubah ke MILIDETIK (ms) biar tidak kecil -> Excel tidak pakai "E"
    brute_ms = (t1 - t0) * 1000.0
    back_ms = (t3 - t2) * 1000.0

    rows.append({
        "Jumlah_Item": n,
        "BruteForce_Kombinasi": brute_checked,
        "Backtracking_Node": back_nodes,
        "Waktu_BruteForce_ms": round(brute_ms, 3),
        "Waktu_Backtracking_ms": round(back_ms, 3),
        "Nilai_Optimal": best_val
    })

result_df = pd.DataFrame(rows)

# Pastikan disimpan sebagai angka desimal biasa (bukan scientific)
# Ini membantu beberapa reader, tapi Excel tetap utama dari besarnya angka (ms sudah aman).
result_df.to_csv(OUTPUT_TABLE, index=False, float_format="%.3f")

# ==============================
# GRAFIK (pakai ms)
# ==============================
plt.figure()
plt.plot(result_df["Jumlah_Item"], result_df["Waktu_BruteForce_ms"], marker="o", label="Brute Force")
plt.plot(result_df["Jumlah_Item"], result_df["Waktu_Backtracking_ms"], marker="o", label="Backtracking")
plt.xlabel("Jumlah Item (n)")
plt.ylabel("Waktu (ms)")
plt.title("Perbandingan Waktu Eksekusi (ms)")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_GRAPH_TIME, dpi=300)
plt.close()

plt.figure()
plt.plot(result_df["Jumlah_Item"], result_df["BruteForce_Kombinasi"], marker="o", label="Brute Force (2^n)")
plt.plot(result_df["Jumlah_Item"], result_df["Backtracking_Node"], marker="o", label="Backtracking (Node)")
plt.xlabel("Jumlah Item (n)")
plt.ylabel("Jumlah Evaluasi")
plt.title("Perbandingan Jumlah Evaluasi")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_GRAPH_NODE, dpi=300)
plt.close()

print("SELESAI (ANTI E). File yang dihasilkan:")
print("-", OUTPUT_TABLE)
print("-", OUTPUT_GRAPH_TIME)
print("-", OUTPUT_GRAPH_NODE)
