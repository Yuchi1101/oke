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
# DATA MSDS TERSTRUKTUR
# ---------------------
msds_data = {
    "Asam & Basa": {
        "HCl": {
            "nama": "Asam Klorida (HCl)",
            "bahaya": "Korosif kuat, menyebabkan luka bakar pada kulit dan mata.",
            "penanganan": "Gunakan sarung tangan tahan asam, pelindung mata, dan masker.",
            "penyimpanan": "Simpan dalam botol kaca/plastik tebal, jauh dari basa.",
            "p3k": "Jika terkena kulit, bilas dengan air selama 15 menit dan cari bantuan medis.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/320331"
        },
        "NaOH": {
            "nama": "Natrium Hidroksida (NaOH)",
            "bahaya": "Sangat korosif, menyebabkan luka bakar kimia.",
            "penanganan": "Gunakan APD lengkap: sarung tangan, goggles, jas lab.",
            "penyimpanan": "Di tempat kering dan tertutup rapat, jauh dari asam.",
            "p3k": "Jika terkena kulit, bilas dengan air banyak dan segera ke IGD.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/221465"
        },
        "H2SO4": {
            "nama": "Asam Sulfat (H2SO4)",
            "bahaya": "Sangat korosif, menghasilkan panas saat bereaksi dengan air.",
            "penanganan": "Tuangkan asam ke air (jangan sebaliknya), gunakan pelindung lengkap.",
            "penyimpanan": "Wadah tahan asam, jauh dari bahan organik dan air.",
            "p3k": "Bilas selama 20 menit, cari pertolongan medis.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/339741"
        }
    },
    "Gas Berbahaya": {
        "NH3": {
            "nama": "Amonia (NH₃)",
            "bahaya": "Gas beracun, menyengat, mengiritasi saluran napas.",
            "penanganan": "Gunakan pelindung pernapasan, pastikan ventilasi cukup.",
            "penyimpanan": "Tabung logam tertutup, jauh dari panas dan asam.",
            "p3k": "Segera bawa ke udara segar, cari bantuan medis.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/aldrich/338818"
        },
        "Cl2": {
            "nama": "Klorin (Cl₂)",
            "bahaya": "Gas kuning-hijau, sangat toksik.",
            "penanganan": "Gunakan respirator, goggles, pastikan ventilasi baik.",
            "penyimpanan": "Silinder baja, jauh dari panas dan bahan reduktor.",
            "p3k": "Evakuasi ke udara segar, beri oksigen bila perlu.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/401279"
        }
    },
    "Pelarut Organik": {
        "Etanol": {
            "nama": "Etanol (C₂H₅OH)",
            "bahaya": "Mudah terbakar, uap menyebabkan pusing.",
            "penanganan": "Gunakan di ruang berventilasi, jauhkan dari api.",
            "penyimpanan": "Wadah tertutup rapat, suhu ruang.",
            "p3k": "Jika kontak mata, bilas. Jika terhirup, ke udara segar.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/aldrich/459836"
        },
        "Aseton": {
            "nama": "Aseton (CH₃COCH₃)",
            "bahaya": "Sangat mudah menguap, menyebabkan iritasi.",
            "penanganan": "Gunakan di lemari asam atau ruang ventilasi baik.",
            "penyimpanan": "Jauhkan dari sumber api dan panas berlebih.",
            "p3k": "Cuci kulit dengan sabun. Jika pusing, ke udara segar.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/650501"
        },
        "Methanol": {
            "nama": "Metanol (CH₃OH)",
            "bahaya": "Beracun, mudah terbakar, bisa sebabkan kebutaan.",
            "penanganan": "Gunakan sarung tangan dan pelindung wajah.",
            "penyimpanan": "Simpan di tempat sejuk, tertutup rapat.",
            "p3k": "Jangan muntah, segera ke rumah sakit.",
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
    Aplikasi ini bertujuan memberikan pemahaman tentang:
    - Risiko senyawa kimia di laboratorium
    - Cara penanganan & penyimpanan aman
    - Akses MSDS asli dari produsen terpercaya

    👉 Tekan *Next* untuk melanjutkan.
    """)
    st.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 2: PENJELASAN UMUM
# ---------------------
elif st.session_state.halaman == 2:
    st.title("📘 Tentang Aplikasi")
    st.markdown("""
    *Apa itu MSDS?*

    Material Safety Data Sheet (MSDS) adalah dokumen resmi yang menjelaskan:
    - Risiko bahan kimia
    - Prosedur penanganan
    - Tindakan P3K dan penyimpanan
    - Link resmi dari produsen

    👉 Tekan *Next* untuk mulai eksplorasi bahan kimia.
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
    st.markdown(f"*Pertolongan Pertama (P3K):* {data['p3k']}")

    if "link" in data:
        st.markdown(f"📎 [🔗 Lihat MSDS Resmi ({senyawa})]({data['link']})")

    col1, col2 = st.columns(2)
    col1.button("⬅ Back", on_click=back)
    col2.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 4: KUIS
# ---------------------
elif st.session_state.halaman == 4:
    st.title("📝 Kuis: Risiko & Penanganan Senyawa Kimia")

    if 'kuis_selesai' not in st.session_state:
        st.session_state.kuis_selesai = False
        st.session_state.skor = 0

    if not st.session_state.kuis_selesai:
        with st.form("form_kuis"):
            st.markdown("### 📌 Data Diri")
            nama = st.text_input("Nama Lengkap")
            kelas = st.text_input("Kelas / Prodi")

            st.markdown("### 1️⃣ Soal Pilihan Ganda")
            pg = [
                {"soal": "Apa fungsi utama MSDS?", "opsi": ["Petunjuk alat", "Informasi bahan kimia", "Laporan analisis", "Metode titrasi"], "jawaban": "Informasi bahan kimia"},
                {"soal": "Etanol termasuk senyawa...", "opsi": ["Asam", "Gas", "Pelarut organik", "Basa"], "jawaban": "Pelarut organik"},
                {"soal": "P3K saat terkena H2SO4 adalah...", "opsi": ["Bilas dengan etanol", "Segera minum air", "Bilas air mengalir lama", "Oleskan basa"], "jawaban": "Bilas air mengalir lama"},
                {"soal": "Penyimpanan NaOH sebaiknya...", "opsi": ["Dekat asam", "Ruang terbuka", "Tertutup & kering", "Dicampur air"], "jawaban": "Tertutup & kering"},
                {"soal": "Bahaya utama Klorin (Cl2)?", "opsi": ["Mudah terbakar", "Toksik", "Radioaktif", "Netral"], "jawaban": "Toksik"},
            ]

            skor_pg = 0
            jawaban_pg = []
            for i, q in enumerate(pg):
                jwb = st.radio(f"{i+1}. {q['soal']}", q["opsi"], key=f"pg{i}")
                jawaban_pg.append((jwb, q["jawaban"]))
                if jwb == q["jawaban"]:
                    skor_pg += 1

            st.markdown("### 2️⃣ Soal Isian")
            isian = [
                {"soal": "Senyawa yang tidak boleh disimpan berdekatan dengan NaOH adalah...", "jawaban": ["asam", "HCl", "H2SO4"]},
                {"soal": "Metanol jika tertelan dapat menyebabkan...", "jawaban": ["kebutaan", "keracunan", "kematian"]},
            ]

            skor_isian = 0
            for i, q in enumerate(isian):
                jawaban = st.text_input(f"{i+1}. {q['soal']}", key=f"isian{i}")
                if jawaban.strip().lower() in [j.lower() for j in q["jawaban"]]:
                    skor_isian += 1

            submitted = st.form_submit_button("✅ Selesai & Lihat Skor")
            if submitted:
                st.session_state.kuis_selesai = True
                st.session_state.skor = skor_pg + skor_isian
                st.session_state.jml_soal = len(pg) + len(isian)

    else:
        st.success(f"✅ Kuis Selesai!\n\n*Skor Anda: {st.session_state.skor} / {st.session_state.jml_soal}*")
        st.markdown("### 🔍 Kunci Jawaban:")
        for i, q in enumerate(pg):
            st.markdown(f"{i+1}. {q['soal']}")
            st.markdown(f"✅ Jawaban Benar: {q['jawaban']}")

        for i, q in enumerate(isian):
            st.markdown(f"*Isian {i+1}: {q['soal']}*")
            st.markdown(f"✅ Contoh jawaban: {q['jawaban'][0]}")

    st.button("⬅ Back", on_click=back)
