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
msds_data = {
    "Asam & Basa": {
        "HCl": {
            "nama": "Asam Klorida (HCl)",
            "bahaya": "Korosif kuat, menyebabkan luka bakar.",
            "penanganan": "Gunakan sarung tangan tahan asam, goggles.",
            "penyimpanan": "Jauh dari basa dan panas.",
            "p3k": "Bilas dengan air mengalir selama 15 menit.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/320331"
        },
        "NaOH": {
            "nama": "Natrium Hidroksida (NaOH)",
            "bahaya": "Sangat korosif, merusak jaringan.",
            "penanganan": "Gunakan APD lengkap.",
            "penyimpanan": "Tempat kering & tertutup, jauh dari asam.",
            "p3k": "Bilas air banyak dan cari bantuan medis.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/221465"
        },
        "H2SO4": {
            "nama": "Asam Sulfat (H2SO4)",
            "bahaya": "Sangat korosif, menghasilkan panas jika dicampur air.",
            "penanganan": "Tuangkan asam ke air, jangan sebaliknya.",
            "penyimpanan": "Wadah tahan asam, jauh dari bahan organik.",
            "p3k": "Bilas lama & cari pertolongan medis.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/339741"
        }
    },
    "Gas Berbahaya": {
        "NH3": {
            "nama": "Amonia (NH₃)",
            "bahaya": "Gas menyengat, menyebabkan iritasi.",
            "penanganan": "Gunakan respirator.",
            "penyimpanan": "Silinder tertutup, jauh dari panas.",
            "p3k": "Segera ke udara segar.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/aldrich/338818"
        },
        "Cl2": {
            "nama": "Klorin (Cl₂)",
            "bahaya": "Toksik, mengiritasi saluran pernapasan.",
            "penanganan": "Gunakan APD dan ventilasi baik.",
            "penyimpanan": "Silinder logam, jauh dari panas.",
            "p3k": "Evakuasi & beri oksigen jika perlu.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/401279"
        }
    },
    "Pelarut Organik": {
        "Etanol": {
            "nama": "Etanol (C₂H₅OH)",
            "bahaya": "Mudah terbakar, uap berbahaya.",
            "penanganan": "Gunakan ruang berventilasi.",
            "penyimpanan": "Tertutup, suhu ruang.",
            "p3k": "Ke udara segar, bilas jika kontak kulit.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/aldrich/459836"
        },
        "Aseton": {
            "nama": "Aseton (CH₃COCH₃)",
            "bahaya": "Mudah menguap dan terbakar.",
            "penanganan": "Gunakan lemari asam.",
            "penyimpanan": "Jauh dari api.",
            "p3k": "Segera bilas dan ke udara segar.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/650501"
        },
        "Methanol": {
            "nama": "Metanol (CH₃OH)",
            "bahaya": "Beracun, menyebabkan kebutaan.",
            "penanganan": "Gunakan pelindung wajah.",
            "penyimpanan": "Tempat sejuk, tertutup.",
            "p3k": "Jangan dimuntahkan, ke RS segera.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/34860"
        }
    }
}

# ---------------------
# HALAMAN 1: BERANDA
# ---------------------
if st.session_state.halaman == 1:
    st.title("💻 Web Pengenalan Risiko dan Cara Menangani Senyawa Kimia Umum")
    st.markdown("### 👥 Kelompok 3 - Kimia Dasar Praktikum")
    st.image("https://images.unsplash.com/photo-1581093448796-8a04b3e1e997", use_column_width=True)
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
            for i, q in enumerate(pg):
                jwb = st.radio(f"{i+1}. {q['soal']}", q["opsi"], key=f"pg{i}")
                if jwb == q["jawaban"]:
                    skor_pg += 1

            st.markdown("### ✍ Soal Isian")
            isian = [
                {"soal": "Apa bahaya utama dari HCl?", "jawaban": ["korosif", "iritasi", "membakar"]},
                {"soal": "Mengapa H2SO4 tidak boleh dituangkan ke air?", "jawaban": ["eksoterm", "panas", "reaksi eksoterm"]},
            ]
            skor_isian = 0
            for i, q in enumerate(isian):
                jawaban = st.text_input(f"{i+1}. {q['soal']}", key=f"isian{i}")
                if jawaban.strip().lower() in [x.lower() for x in q["jawaban"]]:
                    skor_isian += 1

            submitted = st.form_submit_button("✅ Submit")
            if submitted:
                st.session_state.kuis_selesai = True
                st.session_state.skor = skor_pg + skor_isian
                st.session_state.jml_soal = len(pg) + len(isian)

    else:
        st.success(f"🎉 Skor Akhir: {st.session_state.skor} / {st.session_state.jml_soal}")
        st.markdown("### 📖 Kunci Jawaban")
        for i, q in enumerate(pg):
            st.markdown(f"{i+1}. {q['soal']}")
            st.markdown(f"✅ Jawaban Benar: {q['jawaban']}")
        for i, q in enumerate(isian):
            st.markdown(f"*Isian {i+1}: {q['soal']}*")
            st.markdown(f"✅ Contoh Jawaban: {q['jawaban'][0]}")

        if st.button("🏠 Kembali ke Halaman Awal"):
            st.session_state.halaman = 1
            st.session_state.kuis_selesai = False
