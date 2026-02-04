import streamlit as st

st.set_page_config(
    page_title="Daftar Pustaka",
    page_icon="📚",
    layout="wide"
)

# =========================
# STYLE: RAPAT & RATA KIRI
# =========================
st.markdown("""
<style>
.ref-item {
    text-align: left;
    line-height: 1.35;
    margin-bottom: 6px;
    font-size: 0.95rem;
}
.ref-item:hover {
    background-color: #f7f7f7;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '## 📚 Daftar Pustaka (Web <a href="https://forecasting-djp.streamlit.app/" target="_blank">Forecasting</a>)',
    unsafe_allow_html=True
)

st.caption("Daftar referensi penelitian beserta tautan unduh dan pratinjau dokumen.")


# =========================
# DATA REFERENSI (LENGKAP)
# =========================
references = [
    {
        "author": "Ademmer, M. & Boysen-Hogrefe, J.",
        "year": 2022,
        "title": "The Impact of Forecast Errors on Fiscal Planning and Debt Accumulation",
        "source": "Jahrbucher fur Nationalokonomie und Statistik, 242(2), 171–190",
        "url": ""
    },
    {
        "author": "Aggarwal, C.C.",
        "year": 2015,
        "title": "Data Mining: The Textbook",
        "source": "Springer",
        "url": ""
    },
    {
        "author": "Ajder, A., Hamza, H.A.A. & Ayaz, R.",
        "year": 2024,
        "title": "Wavelet-Enhanced Hybrid LSTM-XGBoost Model for Predicting Time Series Containing Unpredictable Events",
        "source": "",
        "url": ""
    },
    {
        "author": "Alm, J. & Torgler, B.",
        "year": 2011,
        "title": "Do Ethics Matter? Tax Compliance and Morality",
        "source": "Journal of Business Ethics, 101(4), 635–651",
        "url": ""
    },
    {
        "author": "Badan Pusat Statistik",
        "year": 2024,
        "title": "Data Produk Domestik Bruto",
        "source": "Badan Pusat Statistik",
        "url": "https://www.bps.go.id/id/statistics-table/2/MTk1NSMy/-seri-2010--1--pdb-triwulanan-atas-dasar-harga-berlaku-menurut-pengeluaran--milyar-rupiah-.html"
    },
    {
        "author": "Badan Pusat Statistik",
        "year": 2024,
        "title": "Indek Harga Perdagangan Besar",
        "source": "Badan Pusat Statistik",
        "url": "https://www.bps.go.id/id/statistics-table/2/MjQjMg==/indeks-harga-perdagangan-besar-indonesia.html"
    },
    {
        "author": "Bank Indonesia",
        "year": 2024,
        "title": "Data Inflasi Indonesia",
        "source": "Bank Indonesia",
        "url": "https://www.bi.go.id/id/statistik/indikator/data-inflasi.aspx"
    },
    {
        "author": "Beaumont, C., Makridakis, S., Wheelwright, S.C. & McGee, V.E.",
        "year": 1984,
        "title": "Forecasting: Methods and Applications",
        "source": "The Journal of the Operational Research Society, 35(1), 79",
        "url": ""
    },
    {
        "author": "Bergmeir, C., Hyndman, R. & Koo, B.",
        "year": 2018,
        "title": "A note on the validity of cross-validation for evaluating autoregressive time series prediction",
        "source": "Computational Statistics & Data Analysis, 120(C), 70–83",
        "url": ""
    },
    {
        "author": "Botchkarev, A.",
        "year": 2018,
        "title": "Performance Metrics (Error Measures) in Machine Learning Regression, Forecasting and Prognostics: Properties and Typology",
        "source": "",
        "url": ""
    },
    {
        "author": "Box, G.E.P., Jenkins, G.M., Reinsel, G.C. & Ljung, G.M.",
        "year": 2015,
        "title": "Time Series Analysis: Forecasting and Control",
        "source": "Wiley",
        "url": ""
    },
    {
        "author": "Cahyono, N.D., Sumpeno, S. & Setiiadi, E.",
        "year": 2023,
        "title": "Multivariate Time Series for Customs Revenue Forecasting Using LSTM Neural Networks",
        "source": "2023 International Conference on Information Technology and Computing (ICITCOM), 357–362",
        "url": ""
    },
    {
        "author": "Chai, T. & Draxler, R.R.",
        "year": 2014,
        "title": "Root mean square error (RMSE) or mean absolute error (MAE)? – Arguments against avoiding RMSE in the literature",
        "source": "Geosci. Model Dev., 7(3), 1247–1250",
        "url": ""
    },
    {
        "author": "Chapman, P., Clinton, J., Randy, K., Thomas, K., Reinartz, T., Shearer, C. & Rüdiger, W.",
        "year": 2000,
        "title": "Step-by-step data mining guide",
        "source": "SPSS inc, 78",
        "url": ""
    },
    {
        "author": "Chen, T. & Guestrin, C.",
        "year": 2016,
        "title": "XGBoost: A scalable tree boosting system",
        "source": "Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, vols 13-17-August-2016, 785–794, Association for Computing Machinery",
        "url": ""
    },
    {
        "author": "Chen, X.-W. & Lin, X.",
        "year": 2014,
        "title": "Big Data Deep Learning: Challenges and Perspectives",
        "source": "IEEE Access, 2, 514–525",
        "url": ""
    },
    {
        "author": "Clemen, R.T.",
        "year": 1989,
        "title": "Combining forecasts: A review and annotated bibliography",
        "source": "International Journal of Forecasting, 5(4), 559–583",
        "url": ""
    },
    {
        "author": "Demšar, J.",
        "year": 2006,
        "title": "Statistical Comparisons of Classifiers over Multiple Data Sets",
        "source": "vol. 7",
        "url": "https://drive.google.com/file/d/1ZVvr5oqPcvMkVeFWmkIVF0nGboSHR2pt/view?usp=drive_link"
    },
    {
        "author": "Diebold, F.X. & Mariano, R.S.",
        "year": 1995,
        "title": "Comparing Predictive Accuracy",
        "source": "Journal of Business & Economic Statistics, 13(3), 253–263",
        "url": ""
    },
    {
        "author": "Direktorat Jenderal Pajak",
        "year": 2022,
        "title": "Surat Edaran Nomor SE-05/PJ/2022 Tentang Pengawasan Kepatuhan Wajib Pajak",
        "source": "",
        "url": ""
    },
    {
        "author": "Fathoni, M.I. & Saputra, A.",
        "year": 2023,
        "title": "Forecasting Value-Added Tax (VAT) revenue using Autoregressive Integrated Moving Average (ARIMA) Box-Jenkins method",
        "source": "Scientax, 4(2), 205–218",
        "url": ""
    },
    {
        "author": "Fayyad, U., Piatetsky-Shapiro, G. & Smyth, P.",
        "year": 1996,
        "title": "From Data Mining to Knowledge Discovery in Databases) (© AAAI)",
        "source": "vol. 17",
        "url": ""
    },
    {
        "author": "Frawley, W.J., Piatetsky-Shapiro, G. & Matheus, C.J.",
        "year": 1992,
        "title": "Knowledge Discovery in Databases: An Overview",
        "source": "",
        "url": ""
    },
    {
        "author": "Gers, F., Schmidhuber, J. & Cummins, F.",
        "year": 2000,
        "title": "Learning to Forget: Continual Prediction with LSTM",
        "source": "Neural Computation, 12, 2451–2471",
        "url": ""
    },
    {
        "author": "Gujarati & Porter",
        "year": 2009,
        "title": "The McGraw-Hill Series Economics",
        "source": "",
        "url": ""
    },
    {
        "author": "Han, Jiawei, Kamber & Micheline",
        "year": 2006,
        "title": "Data Mining: Concepts and Techniques Second Edition",
        "source": "",
        "url": ""
    },
    {
        "author": "Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D. & Meger, D.",
        "year": 2022,
        "title": "Deep Reinforcement Learning that Matters",
        "source": "",
        "url": ""
    },
    {
        "author": "Hewamalage, H., Ackermann, K. & Bergmeir, C.",
        "year": 2022,
        "title": "Forecast Evaluation for Data Scientists: Common Pitfalls and Best Practices",
        "source": "",
        "url": ""
    },
    {
        "author": "Hin, C., Wong, J. & La, N.",
        "year": 2024,
        "title": "Applying machine learning in tax revenue forecasting",
        "source": "",
        "url": ""
    },
    {
        "author": "Hochreiter, S. & Schmidhuber, J.",
        "year": 1997,
        "title": "Long Short-Term Memory",
        "source": "Neural Computation, 9, 1735–1780",
        "url": ""
    },
    {
        "author": "Hyndman, R.J. & Athanasopoulos, G.",
        "year": 2018,
        "title": "Forecasting: principles and practice",
        "source": "OTexts",
        "url": ""
    },
    {
        "author": "Jayanti, D., Sulistyo, S. & Santosa, P.I.",
        "year": 2025,
        "title": "Forecasting Tax Revenue in Indonesia using Single and Hybrid Methods",
        "source": "ICADEIS 2025 - 2025 International Conference on Advancement in Data Science, E-learning and Information System: Integrating Data Science and Information System, Proceeding, Institute of Electrical and Electronics Engineers Inc.",
        "url": ""
    },
    {
        "author": "Jeaab, K., Saoudi, Y. & Falloul, M.E.M.",
        "year": 2024,
        "title": "A Comparison of LSTM, GRU, and XGBoost for forecasting Morocco’s yield curve",
        "source": "Mathematical Modeling and Computing, 11(3), 674–681",
        "url": ""
    },
    {
        "author": "Kahveci, M. & Sabaj, E.",
        "year": 2018,
        "title": "Forecasting tax revenues in an emerging economy: The case of Albania",
        "source": "",
        "url": ""
    },
    {
        "author": "Kementerian Keuangan",
        "year": 2025,
        "title": "SP-42_APBN-2025-Pemerintah-Akselerasi-Pertumbuhan-Ekonomi-yang-Inklusif-dan-Berkelanjutan",
        "source": "",
        "url": ""
    },
    {
        "author": "Kementerian Keuangan & Direktorat Jenderal Perbendaharaan",
        "year": 2024,
        "title": "Pedoman_Teknis_Proyeksi_Penerimaan_dan_Pengeluaran_APBN_Versi_Konsol_06_Final.pdf",
        "source": "",
        "url": ""
    },
    {
        "author": "Kementerian Perdagangan",
        "year": 2024,
        "title": "Data Produk Domestik Bruto",
        "source": "Kementerian Perdagangan",
        "url": "https://satudata.kemendag.go.id/data-informasi/perdagangan-dalam-negeri/produk-domestik-bruto"
    },
    {
        "author": "Khashei, M. & Bijari, M.",
        "year": 2011,
        "title": "A novel hybridization of artificial neural networks and ARIMA models for time series forecasting",
        "source": "Applied Soft Computing, 11(2), 2664–2675",
        "url": ""
    },
    {
        "author": "Kolambe, M. & Arora, S.",
        "year": 2024,
        "title": "Forecasting the Future: A Comprehensive Review of Time Series Prediction Techniques",
        "source": "vol. 20",
        "url": ""
    },
    {
        "author": "Laghrissi, F.E., Douzi, S., Douzi, K. & Hssina, B.",
        "year": 2021,
        "title": "Intrusion detection systems using long short-term memory (LSTM)",
        "source": "Journal of Big Data, 8(1)",
        "url": ""
    },
    {
        "author": "Lestari, T. & Wicaksono, M.",
        "year": 2017,
        "title": "Effect Of Awareness, Knowledge And Attitude Of Taxpayers Tax Compliance For Taxpayers In Tax Service Office Boyolali",
        "source": "vol. 1",
        "url": ""
    },
    {
        "author": "Li, Y., Zhang, R., Zhao, P. & Wei, Y.",
        "year": 2024,
        "title": "Feature-Attended Federated LSTM for Anomaly Detection in the Financial Internet of Things †",
        "source": "Applied Sciences (Switzerland), 14(13)",
        "url": ""
    },
    {
        "author": "Liwei, T., Li, F., Yu, S. & Yuankai, G.",
        "year": 2021,
        "title": "Forecast of LSTM-XGBoost in stock price based on Bayesian optimization",
        "source": "Intelligent Automation and Soft Computing, 29(3), 855–868",
        "url": ""
    },
    {
        "author": "Makridakis, S., Spiliotis, E. & Assimakopoulos, V.",
        "year": 2018,
        "title": "Statistical and Machine Learning forecasting methods: Concerns and ways forward",
        "source": "PLOS ONE, 13(3), e0194889-",
        "url": ""
    },
    {
        "author": "Makridakis, S., Spiliotis, E. & Assimakopoulos, V.",
        "year": 2022,
        "title": "M5 accuracy competition: Results, findings, and conclusions",
        "source": "International Journal of Forecasting, 38(4), 1346–1364",
        "url": ""
    },
    {
        "author": "Mangoting, Y.",
        "year": 2019,
        "title": "Taxpayer Compliance Model Based On Transparency, Ethics, And Trust",
        "source": "vol. 19",
        "url": ""
    },
    {
        "author": "Mardiasmo, M.",
        "year": 2018,
        "title": "Perpajakan Edisi Terbaru 2018",
        "source": "Penerbit Andi. Yogyakarta",
        "url": ""
    },
    {
        "author": "Maryantika, D.D. & Wijaya, S.",
        "year": 2022,
        "title": "Determinants of tax revenue in Indonesia with economic growth as a mediation variable",
        "source": "JPPI (Jurnal Penelitian Pendidikan Indonesia), 8(2), 450",
        "url": ""
    },
    {
        "author": "Moch Firman Firdaus, R. Dimas Adityo & Mas Nurul Hamidah",
        "year": 2022,
        "title": "Peramalan Potensi Perolehan Pajak Daerah Menggunakan Metode Double Exponential Smoothing",
        "source": "Journal of Technology and Informatics (JoTI), 3(2), 49–54",
        "url": ""
    },
    {
        "author": "Myttenaere, A. de, Golden, B., Grand, B. Le & Rossi, F.",
        "year": 2016,
        "title": "Mean Absolute Percentage Error for regression models",
        "source": "Neurocomputing, 192, 38–48",
        "url": ""
    },
    {
        "author": "Nurhaliza, A., Saputra, A., Mirtawati, &, Sains, F. & Teknologi, D.",
        "year": 2024,
        "title": "Evaluasi Akurasi Value at Risk Metode Simulasi Historis melalui Backtesting pada Saham BBCA Tahun 2024",
        "source": "",
        "url": ""
    },
    {
        "author": "Oukhouya, H., Kadiri, H., Himdi, K. El & Guerbaz, R.",
        "year": 2024,
        "title": "Forecasting International Stock Market Trends: XGBoost, LSTM, LSTM-XGBoost, And Backtesting XGBoost Models",
        "source": "Statistics, Optimization and Information Computing, 12(1), 200–209",
        "url": ""
    },
    {
        "author": "Peraturan Direktur Jenderal Perbendaharaan",
        "year": 2024,
        "title": "Petunjuk Teknis Penilaian Indikator Kinerja Pelaksanaan Anggaran Belanja Kementerian Negara / Lembaga",
        "source": "",
        "url": ""
    },
    {
        "author": "Pineau, J., Vincent-Lamarre, P., Sinha, K., Larivière, V., Beygelzimer, A., D’Alché-Buc, F., Fox, E. & Larochelle, H.",
        "year": 2021,
        "title": "Improving Reproducibility in Machine Learning Research",
        "source": "Journal of Machine Learning Research, 22(1)",
        "url": ""
    },
    {
        "author": "Priandono, Y.A. &  Eka Prasetya, M.",
        "year": 2025,
        "title": "Dekomposisi Penerimaan Pajak di Indonesia untuk Meningkatkan Peramalan Estimasi Basis Pajak",
        "source": "Owner : Riset dan Jurnal Akuntansi, 9(1), 130–139",
        "url": ""
    },
    {
        "author": "Putra, R., Sinurat, P., Keuangan, P., Stan, N. & Korespondensi, A.",
        "year": 2023,
        "title": "Potensi Penerimaan Pajak Penghasilan Di Indonesia: Sebuah Analisis Deret Waktu",
        "source": "",
        "url": ""
    },
    {
        "author": "Rokach, L.",
        "year": 2010,
        "title": "Ensemble-based classifiers",
        "source": "Artificial Intelligence Review, 33(1), 1–39",
        "url": ""
    },
    {
        "author": "Shearer, C.",
        "year": 2000,
        "title": "The CRISP-DM model: The new blueprint for data mining",
        "source": "Journal of Data Warehousing, 5, 13-22.",
        "url": ""
    },
    {
        "author": "Siahaan, F.O.P.",
        "year": 2005,
        "title": "The Influence Of Tax Fairness, Ethical Attitudes And Commitment On Taxpayer Compliance Behavior",
        "source": "",
        "url": ""
    },
    {
        "author": "Slemrod, J.",
        "year": 2019,
        "title": "Tax Compliance and Enforcement",
        "source": "Journal of Economic Literature, 57(4), 904–954",
        "url": ""
    },
    {
        "author": "Streimikiene, D., Raheem Ahmed, R., Vveinhardt, J., Ghauri, S.P. & Zahid, S.",
        "year": 2018,
        "title": "Forecasting tax revenues using time series techniques–a case of Pakistan",
        "source": "Economic Research-Ekonomska Istrazivanja , 31(1), 722–754",
        "url": ""
    },
    {
        "author": "Sumanjoyo Hutagalung, S. & Dedy Hermawan, dan",
        "year": 2023,
        "title": "Trend Realisasi Pajak Daerah: Forecasting Analysis",
        "source": "AFRE Accounting and Financial Review, 6(1), 77–85",
        "url": ""
    },
    {
        "author": "Tahar, A. & Bandi, B.",
        "year": 2024,
        "title": "Determinants of enforced and voluntary tax compliance: Adopting slippery slope framework",
        "source": "Journal of Accounting and Investment, 25(2), 621–636",
        "url": ""
    },
    {
        "author": "Tan, P.-N., Steinbach, M., Karpatne, A. & Kumar, V.",
        "year": 2018,
        "title": "Introduction to Data Mining (2nd Edition)",
        "source": "2nd edn., Pearson",
        "url": ""
    },
    {
        "author": "Taufik, R., Aristoteles, A. & Ilman, I.S.",
        "year": 2025,
        "title": "A hybrid model to mitigate data gaps and fluctuations in tax revenue forecasting",
        "source": "International Journal of Electrical and Computer Engineering (IJECE), 15(4), 4099",
        "url": ""
    },
    {
        "author": "Wang, Y., Zhang, N. & Chen, X.",
        "year": 2020,
        "title": "A short-term residential load forecasting model based on lstm recurrent neural network considering weather features",
        "source": "Energies, 14(10)",
        "url": ""
    },
    {
        "author": "Willmott, C.J. & Matsuura, K.",
        "year": 2005,
        "title": "Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance",
        "source": "Climate Research, 30, 79–82",
        "url": ""
    },
    {
        "author": "Wirth, R. & Hipp, J.",
        "year": 2000,
        "title": "CRISP-DM: Towards a standard process model for data mining",
        "source": "Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining",
        "url": ""
    },
    {
        "author": "Witten, I.H., Frank, E., Hall, M.A. & Pal, C.J.",
        "year": 2016,
        "title": "Data Mining, Fourth Edition: Practical Machine Learning Tools and Techniques",
        "source": "4th edn., Morgan Kaufmann Publishers Inc., San Francisco, CA, USA",
        "url": ""
    },
    {
        "author": "Wolpert, D.H.",
        "year": 1992,
        "title": "Stacked generalization",
        "source": "Neural Networks, 5(2), 241–259",
        "url": "https://drive.google.com/file/d/1_8-1RvuvoMEbM0JEYLZqt0bSEVN8lx58/view?usp=drive_link"
    },
    {
        "author": "Yatri, A. & Permana, D.",
        "year": 2019,
        "title": "Peramalan Penerimaan Pajak Negara Indonesia Tahun 2019 Menggunakan Metode Pemulusan Eksponensial Ganda Tipe Brown",
        "source": "",
        "url": ""
    },
    {
        "author": "Zebari, R.R., Zebari, G.M., Al-zebari, A. & Mohammed, M.A.",
        "year": 2025,
        "title": "LSTM-XGBoost: An Ensemble Model for Blood Demand Distribution Forecasting – A Case Study in Zakho City, Kurdistan Region, Iraq",
        "source": "Operations Research Forum, 6(1), 14",
        "url": ""
    },
    {
        "author": "Zhang, G.P.",
        "year": 2003,
        "title": "Time series forecasting using a hybrid ARIMA and neural network model",
        "source": "Neurocomputing, 50, 159–175",
        "url": ""
    },
    {
        "author": "Zhu, L.",
        "year": 2022,
        "title": "Methodology and Application of Fiscal and Tax Forecasting Analysis Based on Multi-Source Big Data Fusion",
        "source": "Mathematical Problems in Engineering, 2022",
        "url": ""
    }
]



# =========================
# SEARCH & FILTER
# =========================
years = sorted({r["year"] for r in references})

c1, c2 = st.columns([2, 1])

with c1:
    keyword = st.text_input(
        "Cari (Author / Judul)",
        placeholder="misal: LSTM, pajak, XGBoost"
    )

with c2:
    year_filter = st.multiselect(
        "Tahun",
        years,
        default=years
    )

# gabungkan semua kolom jadi satu text (WAJIB sebelum filter)
for r in references:
    r["text"] = f"{r['author']} {r['title']} {r['source']} {r['year']}"

# FILTER FINAL (TIDAK ERROR)
filtered = [
    r for r in references
    if r["year"] in year_filter
    and (keyword.lower() in r["text"].lower() or keyword == "")
]


st.divider()

# =========================
# DUA KOLOM
# =========================
col_left, col_right = st.columns([3, 2])

with col_left:
    st.subheader("📄 Referensi")
    selected = None

    labels = [f"[{i+1}] {r['text']}" for i, r in enumerate(filtered)]

    choice = st.radio(
        "📄 Referensi",
        options=range(len(filtered)),
        format_func=lambda x: labels[x],
        label_visibility="collapsed"
    )

    selected = filtered[choice] if filtered else None

  
with col_right:
    st.subheader("⬇️ Unduh & Preview")

    if selected:
        st.markdown(f"**{selected['author']} ({selected['year']})**")
        st.markdown(selected["text"])

        st.link_button("⬇️ Unduh Dokumen", selected["url"], use_container_width=True)

        st.markdown("**Preview:**")
        st.components.v1.iframe(selected["url"], height=480)
    else:
        st.info("Klik salah satu referensi di kiri untuk melihat preview.")
