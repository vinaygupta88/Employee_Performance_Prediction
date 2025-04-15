#  Employee Productivity Prediction Using Machine Learning

This project predicts employee productivity levels (Highly Productive, Average, Medium) using workplace input data. It uses a machine learning model trained on real-world data, with a fully responsive Flask web app frontend.

---

## 📂 Project Structure

```
employee-productivity-predictor/
│
├── app.py                  
├── model.pkl              
├── requirements.txt        
├── Procfile                
├── README.md               
│
├── static/
│   └── css/
│       └── style.css      
│   └── js/
│       └── script.js        
│
├── templates/
│   ├── index.html          
│   ├── about.html          
│   ├── predict.html        
│   ├── result.html         
│   ├── navbar.html         
│   └── footer.html         
│
└── data/
    ├── productivity.csv    
    └── train_model.ipynb   # Jupyter notebook for training the model
```

---

## ⚙️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- Bootstrap 3 (Responsive UI)
- HTML5, CSS3, JavaScript (jQuery)
- Gunicorn (for deployment)
- Render (Free hosting)

---

## 💻 How to Run Locally

### 1. Clone the repo
 ''' clone my repo.......'''

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser 🚀

---

## ✍️ Author

Made  by **[Vinay Kumar](https://vinaygupta88.github.io/Myportfolio/)**

---

## 📜 License

This project is open-source and free to use for learning, research, and personal projects. No formal license is attached—just give credit if you find it helpful!
