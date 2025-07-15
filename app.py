import streamlit as st

# ---------------------
# KONFIGURASI
# ---------------------
st.set_page_config(page_title="Web Risiko & Penanganan Bahan Kimia", layout="centered")

# ---------------------
# INISIALISASI SESSION
# ---------------------
if 'halaman' not in st.session_state:
    st.session_state.halaman = 1
if 'kuis_selesai' not in st.session_state:
    st.session_state.kuis_selesai = False
if 'jawaban_pg' not in st.session_state:
    st.session_state.jawaban_pg = {}
if 'jawaban_isian' not in st.session_state:
    st.session_state.jawaban_isian = {}
if 'nama' not in st.session_state:
    st.session_state.nama = ""
if 'nim' not in st.session_state:
    st.session_state.nim = ""

# ---------------------
# FUNGSI NAVIGASI
# ---------------------
def next():
    st.session_state.halaman += 1

def back():
    st.session_state.halaman -= 1

# ---------------------
# TAMPILAN MENU (SIDEBAR)
# ---------------------
with st.sidebar:
    st.markdown("## 🔀 Tampilan Menu ")
    if st.button("🏠 Beranda"):
        st.session_state.halaman = 1
        st.session_state.kuis_selesai = False
    if st.button("📘 Informasi Aplikasi"):
        st.session_state.halaman = 2
        st.session_state.kuis_selesai = False
    if st.button("📄 Daftar Senyawa"):
        st.session_state.halaman = 3
        st.session_state.kuis_selesai = False
    if st.button("📝 Kuis"):
        st.session_state.halaman = 4
        st.session_state.kuis_selesai = False

# ---------------------
# DAFTAR SENYAWA
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
# DATA KUIS
# ---------------------
pg = [
    {"soal": "Fungsi MSDS adalah...", "opsi": ["Label botol", "Panduan eksperimen", "Informasi bahan kimia", "Lembar nilai"], "jawaban": "Informasi bahan kimia"},
    {"soal": "Senyawa Etanol termasuk...", "opsi": ["Asam", "Basa", "Gas", "Pelarut organik"], "jawaban": "Pelarut organik"},
    {"soal": "Bahaya utama Cl2 adalah...", "opsi": ["Inflamasi kulit", "Bau harum", "Toksik", "Flu"], "jawaban": "Toksik"},
    {"soal": "Metanol jika tertelan dapat menyebabkan...", "opsi": ["Sakit perut", "Buta", "Pilek", "Demam"], "jawaban": "Buta"},
    {"soal": "NaOH sebaiknya tidak disimpan dekat dengan...", "opsi": ["Asam", "Air", "Alkohol", "Besi"], "jawaban": "Asam"},
]

isian = [
    {"soal": "Apa bahaya utama dari HCl?", "jawaban": ["korosif", "iritasi", "membakar"]},
    {"soal": "Mengapa H2SO4 tidak boleh dituangkan ke air?", "jawaban": ["eksoterm", "panas", "reaksi eksoterm"]},
]

# ---------------------
# HALAMAN 1: BERANDA
# ---------------------
if st.session_state.halaman == 1:
    st.title("💻 Web Pengenalan Risiko dan Cara Menangani Senyawa Kimia Umum")
    st.markdown("### 👥 Kelompok 10 - LPK")
    st.markdown("""
    Anggota:
    1. Aurellia Syafa Ghania (2460339)
    2. Hafis Dwi Bahariyanto (2460381)
    3. Nabilah Afrina Fatin (2460448)
    4. Raden Siti Nurul Rachma (2460486)
    5. Yuchi Berliana Resti (2460540)
    """)

    st.markdown("""
    👉 Klik Next untuk mulai!
    """)
    st.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 2: PENJELASAN
# ---------------------
elif st.session_state.halaman == 2:
    st.title("📘 Tentang Aplikasi")
    st.markdown("""
   Aplikasi ini dirancang untuk memberikan edukasi mengenai senyawa kimia yang umum digunakan dalam laboratorium maupun industri.

    Pengguna akan mendapatkan informasi mengenai:
    - Bahaya dari masing-masing senyawa
    - Cara penanganan dan penyimpanan yang tepat
    - Prosedur pertolongan pertama (P3K)

    Dilengkapi juga dengan kuis interaktif untuk menguji pemahaman Anda.
    """)
    col1, col2 = st.columns(2)
    col1.button("⬅ Back", on_click=back)
    col2.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 3: SENYAWA KIMIA
# ---------------------
elif st.session_state.halaman == 3:
    st.title("📄 Daftar Senyawa")
    kategori = st.selectbox("Pilih kategori:", list(msds_data.keys()))
    senyawa = st.selectbox("Pilih senyawa:", list(msds_data[kategori].keys()))
    data = msds_data[kategori][senyawa]

    st.subheader(data["nama"])
    st.markdown(f"Bahaya: {data['bahaya']}")
    st.markdown(f"Penanganan: {data['penanganan']}")
    st.markdown(f"Penyimpanan: {data['penyimpanan']}")
    st.markdown(f"P3K: {data['p3k']}")
    st.markdown(f"📄 [Lihat MSDS Lengkap]({data['link']})")

    col1, col2 = st.columns(2)
    col1.button("⬅ Back", on_click=back)
    col2.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 4: KUIS
# ---------------------
elif st.session_state.halaman == 4:
    st.title("📝 Kuis Pengayaan")

    if not st.session_state.kuis_selesai:
        st.session_state.nama = st.text_input("Nama:")
        st.session_state.instansi = st.text_input("Instansi:")

        st.markdown("### Soal Pilihan Ganda")
        for i, soal in enumerate(pg):
            st.session_state.jawaban_pg[i] = st.radio(soal["soal"], soal["opsi"], key=f"pg_{i}")

        st.markdown("### Soal Isian")
        for i, soal in enumerate(isian):
            st.session_state.jawaban_isian[i] = st.text_input(soal["soal"], key=f"isian_{i}")

        if st.button("Kumpulkan Jawaban"):
            st.session_state.kuis_selesai = True
    else:
        benar = 0
        st.markdown(f"Nama: {st.session_state.nama}")
        st.markdown(f"NIM: {st.session_state.nim}")
        st.markdown("---")

        for i, soal in enumerate(pg):
            jwb = st.session_state.jawaban_pg[i]
            kunci = soal["jawaban"]
            st.markdown(f"{i+1}. {soal['soal']}")
            st.write(f"Jawaban kamu: {jwb}")
            st.write(f"Kunci: {kunci}")
            if jwb == kunci:
                benar += 1

        for i, soal in enumerate(isian):
            jwb = st.session_state.jawaban_isian[i].strip().lower()
            kunci_list = soal["jawaban"]
            st.markdown(f"{i+1+len(pg)}. {soal['soal']}")
            st.write(f"Jawaban kamu: {jwb}")
            st.write(f"Kunci kemungkinan: {', '.join(kunci_list)}")
            if jwb in kunci_list:
                benar += 1

        total = len(pg) + len(isian)
        skor = round((benar / total) * 100, 2)
        st.success(f"🎉 Skor Akhir: {skor} / 100")

        if st.button("⬅ Kembali ke Halaman Awal"):
            st.session_state.halaman = 1
            st.session_state.kuis_selesai = False
