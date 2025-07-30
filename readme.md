# 📊 YouTube Channel Analytics: Apna College (ETL + Power BI Dashboard)

End-to-end data engineering and analytics project built to analyze the **Apna College YouTube channel**  
using Python, PostgreSQL, and Power BI.

> 🚀 **Goal:** Build an automated ETL pipeline to extract data, transform it, load into database, and create a dynamic dashboard to gain insights on video performance and engagement.

---

## 🛠 **Tools & Technologies Used**
- Python (pandas, requests, sqlalchemy, python-dotenv)
- PostgreSQL
- Power BI
- Git & GitHub

---

## 📦 **Project Structure**
├── Scripts/ # Python scripts
│ ├── fetch_data.py # Fetch data from YouTube API
│ ├── transform_data.py # Clean & transform data
│ ├── load_data_to_db.py # Load data into PostgreSQL
│ ├── load_data_to_csv.py # Load data into CSV file
├── db/
│ └── connection.py # DB connection script
├── Data/
| └── Processed_data/
|   ├── clean_data.csv
│   ├── structured_data.csv
│   ├── tag_analyzed_data.csv
│   ├── transformed_data.csv
│ └── Raw_data/
│   └── video_data.json # Raw API data
├── Dashboard/
│ ├── YT-Apna-College-Dashboard.pdf # Dashboard export
│ └── YT-Apna-College-Dashboard.pbix # Power BI file
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore


---

## 🔄 **ETL Pipeline Overview**
✅ **Extract:**  
- Fetch video data from YouTube API

✅ **Transform:**  
- Clean, normalize, and enrich data:
  - Parse nested JSON
  - Convert data types
  - Calculate:
    - Engagement rate
    - Views velocity
    - Days since published
  - Analyze tags

✅ **Load:**  
- Load clean & transformed data into PostgreSQL database
- Separate tables: raw, cleaned, transformed, tag analysis

---

## 📊 **Power BI Dashboard**
Built on top of PostgreSQL data:
- KPIs: Total videos, total views, average engagement rate
- Top 10 videos by views
- Views & engagement trends over time
- Likes vs views scatter plot
- Tag analysis: engagement rate with vs without tags
- Detailed video table

> 🧩 **Pages:**  
> 1️⃣ Overview & KPIs  
> 2️⃣ Video Deep Dive  
> 3️⃣ Tag Analysis & Impact

---

## ⚙ **How to Run Locally**

1️⃣ Clone this repo:
    ```bash
    git clone https://github.com/yourusername/YouTube-Channel-Analytics.git

2️⃣ Install dependencies:
    pip install -r requirements.txt

3️⃣ Add your API key & DB config to .env file:
    YOUTUBE_API_KEY=your_key
    CHANNEL_ID=your_channel_id
    DB_USER=your_db_user
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=your_db_name

4️⃣ Run ETL pipeline:
    python Scripts/fetch_data.py
    python Scripts/transform_data.py
    python Scripts/load_data_to_db.py

5️⃣ Open Power BI → connect to PostgreSQL → refresh dashboard


✏ Author

    Md Mudabbir Quamar
🔗 GitHub:      github.com/yourusername
🔗 LinkedIN:    www.linkedin.com/in/mudabbirquamar