import streamlit as st

# ---------------------
# KONFIGURASI HALAMAN
# ---------------------
st.set_page_config(page_title="Web Risiko & Penanganan Bahan Kimia", layout="centered")
if 'halaman' not in st.session_state:
    st.session_state.halaman = 1

def next():
    st.session_state.halaman += 1

def back():
    st.session_state.halaman -= 1

# ---------------------
# NAVIGASI CEPAT (SIDEBAR)
# ---------------------
with st.sidebar:
    st.markdown("## 🔀 Navigasi Cepat")
    if st.button("🏠 Ke Beranda"):
        st.session_state.halaman = 1
        st.session_state.kuis_selesai = False
    if st.button("📘 Tentang"):
        st.session_state.halaman = 2
        st.session_state.kuis_selesai = False
    if st.button("📄 Data MSDS"):
        st.session_state.halaman = 3
        st.session_state.kuis_selesai = False
    if st.button("📝 Kuis"):
        st.session_state.halaman = 4
        st.session_state.kuis_selesai = False

# ---------------------
# DATA MSDS
# ---------------------
# (isi sama seperti sebelumnya, tidak diulang agar tidak terlalu panjang — silakan gunakan bagian msds_data dari skrip kamu)

# ---------------------
# HALAMAN 1: BERANDA
# ---------------------
if st.session_state.halaman == 1:
    st.title("💻 Web Pengenalan Risiko dan Cara Menangani Senyawa Kimia Umum")
    st.markdown("### 👥 Kelompok 3 - Kimia Dasar Praktikum")
    st.image("https://images.unsplash.com/photo-1581093448796-8a04b3e1e997", use_column_width=True)

    st.markdown("#### 👩‍🔬 Anggota Kelompok:")
    st.markdown("""
    1. Ahmad Rizky Pratama (2310001)  
    2. Bella Rahmawati (2310002)  
    3. Chandra Permana (2310003)  
    4. Dwi Lestari (2310004)  
    5. Eka Nurhaliza (2310005)  
    """)

    st.markdown("""
    Aplikasi ini memberikan pemahaman tentang:
    - Risiko bahan kimia
    - Penanganan & penyimpanan yang benar
    - Tautan langsung ke MSDS

    👉 Klik *Next* untuk mulai!
    """)
    st.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 2: PENJELASAN UMUM
# ---------------------
elif st.session_state.halaman == 2:
    st.title("📘 Tentang Aplikasi")
    st.markdown("""
    *MSDS (Material Safety Data Sheet)* adalah dokumen resmi berisi:
    - Bahaya bahan kimia
    - Cara penanganan aman
    - Prosedur P3K dan penyimpanan
    - Tautan ke sumber resmi

    👉 Klik *Next* untuk eksplorasi bahan kimia.
    """)
    col1, col2 = st.columns(2)
    col1.button("⬅ Back", on_click=back)
    col2.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 3: DATA MSDS
# ---------------------
elif st.session_state.halaman == 3:
    st.title("📄 Informasi MSDS Berdasarkan Kategori")

    kategori = st.selectbox("📚 Pilih Kategori Senyawa:", list(msds_data.keys()))
    senyawa = st.selectbox("🧪 Pilih Senyawa:", list(msds_data[kategori].keys()))

    data = msds_data[kategori][senyawa]
    st.subheader(f"📋 MSDS untuk {senyawa}")
    st.markdown(f"*Nama Bahan:* {data['nama']}")
    st.markdown(f"*Bahaya:* {data['bahaya']}")
    st.markdown(f"*Penanganan:* {data['penanganan']}")
    st.markdown(f"*Penyimpanan:* {data['penyimpanan']}")
    st.markdown(f"*P3K:* {data['p3k']}")
    st.markdown(f"📎 [🔗 Lihat MSDS Resmi]({data['link']})")

    col1, col2 = st.columns(2)
    col1.button("⬅ Back", on_click=back)
    col2.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 4: KUIS
# ---------------------
elif st.session_state.halaman == 4:
    st.title("📝 Kuis: Risiko & Penanganan Bahan Kimia")

    if 'kuis_selesai' not in st.session_state:
        st.session_state.kuis_selesai = False
        st.session_state.skor = 0

    if not st.session_state.kuis_selesai:
        with st.form("form_kuis"):
            nama = st.text_input("Nama Lengkap")
            nim = st.text_input("NIM")
            prodi = st.text_input("Kelas / Prodi")

            st.markdown("### 📌 Soal Pilihan Ganda")
            pg = [
                {"soal": "Fungsi MSDS adalah...", "opsi": ["Label botol", "Panduan eksperimen", "Informasi bahan kimia", "Lembar nilai"], "jawaban": "Informasi bahan kimia"},
                {"soal": "Senyawa Etanol termasuk...", "opsi": ["Asam", "Basa", "Gas", "Pelarut organik"], "jawaban": "Pelarut organik"},
                {"soal": "Bahaya utama Cl2 adalah...", "opsi": ["Inflamasi kulit", "Bau harum", "Toksik", "Flu"], "jawaban": "Toksik"},
                {"soal": "Metanol jika tertelan dapat menyebabkan...", "opsi": ["Sakit perut", "Buta", "Pilek", "Demam"], "jawaban": "Buta"},
                {"soal": "NaOH sebaiknya tidak disimpan dekat dengan...", "opsi": ["Asam", "Air", "Alkohol", "Besi"], "jawaban": "Asam"},
            ]

            skor_pg = 0
            jawaban_pg_user = []

            for i, q in enumerate(pg):
                jwb = st.radio(f"{i+1}. {q['soal']}", q["opsi"], key=f"pg{i}")
                jawaban_pg_user.append(jwb)
                if jwb == q["jawaban"]:
                    skor_pg += 1

            st.markdown("### ✍ Soal Isian")
            isian = [
                {"soal": "Apa bahaya utama dari HCl?", "jawaban": ["korosif", "iritasi", "membakar"]},
                {"soal": "Mengapa H2SO4 tidak boleh dituangkan ke air?", "jawaban": ["eksoterm", "panas", "reaksi eksoterm"]},
            ]

            skor_isian = 0
            jawaban_isian_user = []

            for i, q in enumerate(isian):
                jawaban = st.text_input(f"{i+1}. {q['soal']}", key=f"isian{i}")
                jawaban_isian_user.append(jawaban)
                if jawaban.strip().lower() in [x.lower() for x in q["jawaban"]]:
                    skor_isian += 1

            submitted = st.form_submit_button("✅ Submit")
            if submitted:
                st.session_state.kuis_selesai = True
                st.session_state.skor = skor_pg + skor_isian
                st.session_state.jml_soal = len(pg) + len(isian)
                st.session_state.jawaban_pg_user = jawaban_pg_user
                st.session_state.jawaban_isian_user = jawaban_isian_user

    else:
        st.success(f"🎉 Skor Akhir: {st.session_state.skor} / {st.session_state.jml_soal}")
        st.markdown("### 📖 Kunci Jawaban")

        for i, q in enumerate(pg):
            user_jwb = st.session_state.jawaban_pg_user[i]
            benar = "✅" if user_jwb == q['jawaban'] else "❌"
            st.markdown(f"{i+1}. {q['soal']}\n- Jawaban Anda: {user_jwb} {benar}\n- Jawaban Benar: {q['jawaban']}")

        for i, q in enumerate(isian):
            user_isian = st.session_state.jawaban_isian_user[i]
            cocok = user_isian.strip().lower() in [x.lower() for x in q['jawaban']]
            benar = "✅" if cocok else "❌"
            st.markdown(f"*Isian {i+1}: {q['soal']}*\n- Jawaban Anda: {user_isian} {benar}\n- Contoh Jawaban: {q['jawaban'][0]}")

        if st.button("🏠 Kembali ke Halaman Awal"):
            st.session_state.halaman = 1
            st.session_state.kuis_selesai = False
