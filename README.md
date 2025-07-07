# 🧠 MedBot – NLP-Based Medical QA Assistant

MedBot is an intelligent question-answering assistant for biomedical and healthcare-related queries. It uses advanced natural language processing techniques and pretrained models like BioBERT to answer medical questions extracted from trusted sources such as PubMed and MedQuAD.

This project is developed as part of our master's studies in Data Science at TU Darmstadt to gain practical experience in building real-world NLP systems.

---

## 📌 Project Goals

- ✅ Build an **Extractive QA System** using **BioBERT**
- ✅ Use **LangChain** for modular QA pipeline
- ✅ Create an interactive **frontend with Streamlit or Gradio**
- ✅ (Bonus) Add **speech input/output** for accessibility
- ✅ Evaluate the system using QA metrics (EM, F1)

---

## 🧰 Technologies & Tools

| Tool                | Purpose                              |
|---------------------|--------------------------------------|
| Python              | Programming Language                 |
| HuggingFace Transformers | Pretrained NLP models         |
| BioBERT             | Biomedical QA                        |
| LangChain           | QA pipeline building                 |
| Streamlit / Gradio  | Frontend interface                   |
| FAISS / BM25        | Document retrieval                   |
| Docker (optional)   | Deployment container                 |
| Git + GitHub        | Team collaboration                   |
| GitHub Actions      | CI/CD automation                     |

---

## 👨‍💻 Team Members

| Name | GitHub |
|------|--------|
| [Mahmoud Sayed]     | [@MahmoudSayed129](https://github.com/MahmoudSayed129))     |
| [Michael Yassa]     | [@Miichael-Yassa](https://github.com/Miichael-Yassa)     |

---

## 📁 Project Structure

medbot/
├── data/ # Raw & preprocessed medical datasets
├── qa_pipeline/ # BioBERT model + document retriever
├── app/ # Streamlit or Gradio frontend
├── speech/ # Speech-to-text and text-to-speech (optional)
├── eval/ # Evaluation scripts and results
├── requirements.txt # Python dependencies
├── .github/ # GitHub Actions workflows (CI/CD)
│ └── workflows/
│ └── python-app.yml
├── CONTRIBUTING.md # Collaboration workflow
└── README.md # Project documentation

📚 Dataset References
MedQuAD – QA pairs from NIH & NLM

PubMed – Biomedical articles

BioASQ – Optional biomedical QA dataset

