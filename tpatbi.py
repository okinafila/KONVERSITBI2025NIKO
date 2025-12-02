import streamlit as st
from streamlit_option_menu import option_menu
from fpdf import FPDF
import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Nilai Tes Anda', 0, 1, 'C')
def main ():
    st.title("Aplikasi Perhitungan dan Simpan PDF")

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Hitung Nilai Hasil CAT',
    ['Hitung Nilai TPA',
     'Hitung Nilai TBI'],                     
    default_index=1)

# halaman hitung nilai TPA
if (selected == 'Hitung Nilai TPA') :
    st.title ('Hitung Nilai TPA')

# Masukkan nilai-nilai verbal, numerikal, dan figural
    nama = st.text_input ("Nama")
    nilai_verbal = float(st.text_input ("Masukkan Nilai Verbal", 0))
    nilai_numerikal =float(st.text_input ("Masukkan Nilai Numerikal", 0))
    nilai_figural = float(st.text_input ("Masukkan Nilai Figural", 0))

    Hitung = st.button('Hitung Nilai TPA')

    if Hitung :
        rata_rata = (nilai_verbal + nilai_numerikal + nilai_figural) / 3
        nilai_tpa = ((rata_rata / 100)*600)+200
        st.markdown(f'<p style="font-size: 24px;">Nilai TPA Anda Adalah= {round(nilai_tpa, 2)}</p>', unsafe_allow_html=True)
# Simpan hasil dalam PDF
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Courier", size=12)
    # tambah logopkm
        pdf.image("logopusbinjf.png", x=10, y=8, w=25)
        pdf.cell(200, 10, f" ", ln=True, align="C")
    # tambah nama
        pdf.cell(50, 10, "Nama: ")
        pdf.cell(50, 10, str(nama))
        pdf.cell(200, 10, f" ", ln=True)
    # Tambahkan tabel
        pdf.set_font("Courier", "B", 12)
        pdf.cell(50, 10, "Subtest", 1, 0, "C")
        pdf.cell(50, 10, "Nilai", 1, 0, "C")
        pdf.ln()
            
        pdf.set_font("Courier", size=12)
        pdf.cell(50, 10, "Verbal", 1)
        pdf.cell(50, 10, str(nilai_verbal), 1, 0, "C")
        pdf.ln()

        pdf.cell(50, 10, "Numerikal", 1)
        pdf.cell(50, 10, str(nilai_numerikal), 1, 0, "C")
        pdf.ln()

        pdf.cell(50, 10, "Figural", 1)
        pdf.cell(50, 10, str(nilai_figural), 1, 0, "C")
        pdf.ln()
            
        pdf.cell(50, 10, "Skor TPA", 1)
        pdf.cell(50, 10, f"{round(nilai_tpa, 2)}", 1, 0, "C")
        pdf.ln()

        pdf.set_font("Courier", size=11)
        pdf.cell(20, 5, "Note : hasil tes ini bersifat try out, tidak dapat digunakan untuk mengikuti", 0)
        pdf.ln()
        pdf.cell(20, 5, "       seleksi beasiswa apapun", 0)
        pdf.ln()
        
        # Tambahkan kata-kata "Hormat Kami Tim PTT"
        pdf.cell(200, 50, "Best Regards,", ln=True, align="C")
        pdf.cell(200, 10, "Pusbin JFPM", ln=True, align="C")

        pdf.set_y(0)  # Geser posisi ke atas untuk footer
        pdf.cell(0, 10, f"Dicetak: {current_date}", 0, 0, "R")
        pdf_output = pdf.output(dest="S").encode("latin1")

        # Tampilkan tombol download PDF
        st.download_button(
        label="Download Hasil Perhitungan TPA (PDF)",
        data=pdf_output,
        file_name="hasil_perhitungan_tpa.pdf",
        mime="application/pdf"
            )

if (selected == "Hitung Nilai TBI") :
    st.title('Hitung Nilai TBI')

    # Nilai asli dan nilai konversi untuk Listening
    nilai_listening = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
    konversi_listening = [31, 32, 32, 33, 34, 35, 35, 36, 37, 38, 38, 39, 40, 41, 41, 42, 43, 44, 44, 45, 46, 47, 47, 48, 49, 50, 50, 51, 52, 52, 53, 54, 55, 55, 56, 57, 58, 58, 59, 60, 61, 61, 62, 63, 64, 64, 65, 66, 67, 67, 68]

    # Nilai asli dan nilai konversi untuk Structure
    nilai_structure = [0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35, 37.5, 40, 42.5, 45, 47.5, 50, 52.5, 55, 57.5, 60, 62.5, 65, 67.5, 70, 72.5, 75, 77.5, 80, 82.5, 85, 87.5, 90, 92.5, 95, 97.5, 100]
    konversi_structure = [31, 32, 33, 34, 35, 36, 37, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 62, 63, 64, 65, 66, 67, 68]

    # Nilai asli dan nilai konversi untuk Reading
    nilai_reading = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
    konversi_reading = [31,	32,	32,	33,	34,	35,	35,	36,	37,	37,	38,	39,	40,	40,	41,	42,	43,	43,	44,	45,	45,	46,	47,	48,	48,	49,	50,	50,	51,	52,	53,	53,	54,	55,	55,	56,	57,	58,	58,	59,	60,	61,	61,	62,	63,	63,	64,	65,	66,	66,	67]

    # Buat dictionary konversi untuk setiap variabel
    konversi_dict = {
    'Listening': dict(zip(nilai_listening, konversi_listening)),
    'Structure': dict(zip(nilai_structure, konversi_structure)),
    'Reading': dict(zip(nilai_reading, konversi_reading))
    }

    # Fungsi untuk mengkonversi nilai asli ke nilai konversi
    def konversi_nilai(variabel, nilai_asli):
        return konversi_dict[variabel][nilai_asli]


    # Fungsi konversi_nilai dan konversi_dict seperti yang telah diberikan sebelumnya

    # Input nilai dari pengguna
    nama = st.text_input ("Nama")

    nilai_input = float(st.text_input ("Masukkan Nilai Listening", 0))
    nilai_asli = nilai_input
    nilai_konversi_listening = konversi_nilai('Listening', nilai_asli)

    nilai_input1 = float(st.text_input ("Masukkan Nilai Structure", 0))
    nilai_asli = nilai_input1
    nilai_konversi_structure = konversi_nilai('Structure', nilai_asli)

    nilai_input2 = float(st.text_input ("Masukkan Nilai Reading", 0))
    nilai_asli = nilai_input2
    nilai_konversi_reading = konversi_nilai('Reading', nilai_asli)

    # Menghitung nilai akhir
    Hitung = st.button('Hitung Nilai TBI')

    if Hitung :
        nilai_akhir = (nilai_konversi_listening  + nilai_konversi_structure  + nilai_konversi_reading )/3 * 10
        st.markdown(f'<p style="font-size: 24px;">Nilai TBI Anda Adalah= {round(nilai_akhir, 2)}</p>', unsafe_allow_html=True)
    # Kategorisasi nilai TBI ke dalam CEFR level
        def cefr_level_tbi(skor):
            if 627 <= skor <= 677:
                return "C1 : Effective Operational Proficiency / Advanced (Proficient User)"
            elif 543 <= skor <= 626:
                return "B2 : Vantage / Upper Intermediate (Independent User)"
            elif 460 <= skor <= 542:
                return "B1 : Threshold/Intermediate (Independent User)"
            elif 310 <= skor <= 459:
                return "A2: Waystage / Elementary (Basic User)"
            else:
                return "Skor tidak termasuk dalam kategori yang diberikan"

        kategori_cefr = cefr_level_tbi(round(nilai_akhir))

# Simpan hasil dalam PDF
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Courier", size=12)
    # tambah logopkm
        pdf.image("logopusbinjf.png", x=10, y=8, w=25)
        pdf.cell(200, 10, f" ", ln=True, align="C")
    # tambah nama
        pdf.cell(50, 10, "Nama: ")
        pdf.cell(50, 10, str(nama))
        pdf.cell(200, 10, f" ", ln=True)
    # Tambahkan tabel
        pdf.set_font("Courier", "B", 12)
        pdf.cell(50, 10, "Subtest", 1, 0, "C")
        pdf.cell(50, 10, "Nilai Konversi", 1, 0, "C")
        pdf.ln()
            
        pdf.set_font("Courier", size=12)
        pdf.cell(50, 10, "Listening", 1)
        pdf.cell(50, 10, str(nilai_konversi_listening), 1, 0, "C")
        pdf.ln()

        pdf.cell(50, 10, "Structure", 1)
        pdf.cell(50, 10, str(nilai_konversi_structure), 1, 0, "C")
        pdf.ln()

        pdf.cell(50, 10, "Reading", 1)
        pdf.cell(50, 10, str(nilai_konversi_reading), 1, 0, "C")
        pdf.ln()
            
        pdf.cell(50, 10, "Skor TBI", 1)
        pdf.cell(50, 10, f"{round(nilai_akhir, 2)}", 1, 0, "C")
        pdf.ln()

        
        pdf.cell(30, 10, "Kategori :", 0)
        pdf.cell(150, 10, str(kategori_cefr), 0)
        pdf.ln()

        pdf.set_font("Courier", size=11)
        pdf.cell(20, 5, "Note : hasil tes ini bersifat try out, tidak dapat digunakan untuk mengikuti", 0)
        pdf.ln()
        pdf.cell(20, 5, "       seleksi beasiswa apapun", 0)
        pdf.ln()
        # Tambahkan kata-kata "Hormat Kami Tim PTT"
        pdf.set_font("Courier", size=12)
        pdf.cell(200, 50, "Best Regards,", ln=True, align="C")
        pdf.cell(200, 10, "Pusbin JFPM", ln=True, align="C")

        pdf.set_y(0)  # Geser posisi ke atas untuk footer
        pdf.cell(0, 10, f"Dicetak: {current_date}", 0, 0, "R")
        pdf_output = pdf.output(dest="S").encode("latin1")

         
    # Tampilkan tombol download PDF
        st.download_button(
        label="Download Hasil Perhitungan TBI (PDF)",
        data=pdf_output,
        file_name="hasil_perhitungan_tbi.pdf",
        mime="application/pdf"
        )

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2016/10/11/21/43/geometric-1732847_640.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


