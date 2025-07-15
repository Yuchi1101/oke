import streamlit as st

# Setup awal
st.set_page_config(page_title="MSDS Wizard", layout="centered")

# Inisialisasi halaman (default ke 1)
if 'halaman' not in st.session_state:
    st.session_state.halaman = 1

# Tombol Navigasi
def next():
    st.session_state.halaman += 1

def back():
    st.session_state.halaman -= 1

# -------------------------
# DATA MSDS
# -------------------------
msds_dict = {
    "HCl": {
        "nama": "Asam Klorida",
        "bahaya": "Korosif, mengiritasi saluran pernapasan.",
        "penanganan": "Gunakan APD lengkap, hindari kontak langsung.",
        "penyimpanan": "Di tempat berventilasi, jauh dari basa.",
        "p3k": "Bilas air mengalir jika terkena kulit. Segera cari bantuan medis."
    },
    "NaOH": {
        "nama": "Natrium Hidroksida",
        "bahaya": "Sangat korosif, merusak jaringan hidup.",
        "penanganan": "Gunakan sarung tangan dan pelindung mata.",
        "penyimpanan": "Simpan di tempat kering, jauh dari asam.",
        "p3k": "Cuci dengan air mengalir, segera ke fasilitas medis."
    },
    "Etanol": {
        "nama": "Etanol",
        "bahaya": "Mudah terbakar, dapat mengiritasi mata.",
        "penanganan": "Jauhkan dari panas dan api, ventilasi cukup.",
        "penyimpanan": "Wadah tertutup rapat, suhu ruang.",
        "p3k": "Jika terhirup, pindah ke udara segar. Jika kontak mata, bilas air."
    }
}

# -------------------------
# HALAMAN 1: BERANDA
# -------------------------
if st.session_state.halaman == 1:
    st.title("🧪 Aplikasi MSDS Bahan Kimia")
    st.markdown("### Selamat Datang!")
    st.image("https://raw.githubusercontent.com/Yuchi1101/oke/refs/heads/main/10002208760.jpg", use_column_width=True)
    st.markdown("""
        Aplikasi ini menyediakan informasi MSDS untuk beberapa bahan kimia umum.
        Tekan *Next* untuk memulai.
    """)
    st.button("Next ▶", on_click=next)

# -------------------------
# HALAMAN 2: PENJELASAN
# -------------------------
elif st.session_state.halaman == 2:
    st.title("📋 Tentang Aplikasi")
    st.markdown("""
    *Apa itu MSDS?*  
    Material Safety Data Sheet (MSDS) adalah dokumen penting yang menjelaskan:
    - ✅ Bahaya bahan kimia
    - ✅ Cara penanganan aman
    - ✅ Penyimpanan dan pertolongan pertama

    Tekan *Next* untuk melihat data bahan kimia.
    """)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("⬅ Back", on_click=back)
    with col2:
        st.button("Next ▶", on_click=next)

# -------------------------
# HALAMAN 3: PILIH & LIHAT MSDS
# -------------------------
elif st.session_state.halaman == 3:
    st.title("📄 Lihat MSDS Bahan Kimia")
    bahan = st.selectbox("Pilih bahan kimia:", list(msds_dict.keys()))

    if bahan:
        data = msds_dict[bahan]
        st.subheader(f"Informasi MSDS untuk {bahan}")
        st.markdown(f"*Nama Bahan:* {data['nama']}")
        st.markdown(f"*Bahaya:* {data['bahaya']}")
        st.markdown(f"*Penanganan:* {data['penanganan']}")
        st.markdown(f"*Penyimpanan:* {data['penyimpanan']}")
        st.markdown(f"*Pertolongan Pertama (P3K):* {data['p3k']}")

    st.button("⬅ Back", on_click=back)
