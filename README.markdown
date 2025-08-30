# Enhancing Linux Process Scheduling with Machine Learning Techniques

## 📌 Project Overview
Linux uses different process scheduling algorithms (CFS, Round Robin, Priority-based, etc.) to manage CPU time between processes. While these schedulers are efficient, they are based on static heuristics and cannot dynamically adapt to workload variations.

This project explores how machine learning techniques can be applied to enhance Linux process scheduling. By predicting CPU burst times and resource requirements, we can:

- Reduce context switches
- Improve CPU utilization
- Optimize turnaround and waiting times
- Increase overall system throughput

In simple terms, the scheduler becomes "intelligent", making better decisions based on predictions rather than fixed rules.

## ⚙️ Features
- Collects process-related features (arrival time, burst time, priority, etc.)
- Uses machine learning models to predict next CPU burst
- Simulates scheduling decisions with and without ML
- Provides visualizations (graphs, tables, metrics) for comparison
- Frontend interface for result visualization

## 🏗️ Project Architecture
```
    +------------------+
    |  Data Collection |
    +------------------+
             |
             v
    +---------------------+
    |  ML Model Training  |
    +---------------------+
             |
             v
    +----------------------+
    | Scheduler Simulation |
    +----------------------+
             |
             v
    +-------------------------+
    | Results & Visualization |
    +-------------------------+
```

- **Backend** (Python, Jupyter, ML libraries)
  - Data preprocessing
  - Training models (Decision Tree, Random Forest, etc.)
  - Running simulations
- **Frontend** (HTML, CSS/SCSS, JS)
  - Displays metrics like turnaround time, waiting time, throughput
  - Graphs for comparison between default Linux scheduler and ML-based scheduler

## 📂 Project Structure
```
├── backend/
│   ├── train_ml_model.py       # ML model training
│   ├── run_scheduler.py        # Scheduler simulation with ML
│   ├── notebooks/              # Jupyter notebooks for experiments
│   ├── models/                 # Saved ML models
│   └── data/                   # Datasets (process traces)
│
├── frontend/
│   ├── index.html              # Web UI
│   ├── style.scss / style.css  # Styling
│   ├── script.js               # Visualizations
│
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
└── LICENSE                     # License (MIT / Apache)
```

## 🔧 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/21AG1A05F0/Enhancing-Linux-Process-Scheduling-with-Machine-Learning-Techniques.git
   cd Enhancing-Linux-Process-Scheduling-with-Machine-Learning-Techniques
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   💡 **If requirements.txt is missing:**
   Install manually with:
   ```bash
   pip install numpy pandas scikit-learn matplotlib
   ```
   Then generate one:
   ```bash
   pip freeze > requirements.txt
   ```

4. **Run the Backend (Model Training + Simulation)**
   ```bash
   python backend/train_ml_model.py
   python backend/run_scheduler.py
   ```

5. **Run the Frontend (Visualization)**
   ```bash
   cd frontend
   # Option 1: Python simple server
   python3 -m http.server 8000
   # Option 2: Node.js live server
   live-server
   ```
   Now open 👉 http://localhost:8000 in your browser.

## 🚀 Usage
1. **Train the Model**
   ```bash
   python backend/train_ml_model.py --dataset backend/data/process_dataset.csv
   ```
   ➡️ Saves trained model into `backend/models/`

2. **Run Scheduler Simulation**
   ```bash
   python backend/run_scheduler.py --model backend/models/scheduler_model.pkl
   ```
   ➡️ Generates metrics like turnaround time, waiting time, CPU utilization.

3. **Visualize Results**
   - Open `frontend/index.html` in a browser
   - View performance comparison graphs

## 📊 Evaluation & Results
**Baseline (Linux Scheduler) vs ML-based Scheduler**

**Metrics evaluated:**
- Average Waiting Time
- Average Turnaround Time
- Number of Context Switches
- Throughput

**Example Outcomes** (Replace with your actual results)
- ML-based reduced context switches by 18%
- Waiting time reduced by 12%
- CPU utilization increased by 9%

## 🔮 Future Scope
- Integrate ML scheduler directly into Linux kernel (CFS patching)
- Explore deep learning models (LSTM, GRU) for burst prediction
- Handle I/O-bound processes along with CPU-bound
- Test with real system workloads instead of synthetic datasets
- Extend to multi-core / multiprocessor scheduling

## 🤝 Contributing
Contributions are welcome!

1. Fork the repo
2. Create a feature branch
   ```bash
   git checkout -b feature-xyz
   ```
3. Commit changes
   ```bash
   git commit -m "Added feature xyz"
   ```
4. Push to your fork
   ```bash
   git push origin feature-xyz
   ```
5. Open a Pull Request 🎉