# NYC Taxi Data Engineering Pipeline 🚖

A complete real-time data engineering pipeline that ingests, processes, stores, and analyzes NYC Yellow Taxi trip data. The pipeline is built using Apache Kafka, Apache Spark Structured Streaming, PostgreSQL, and Apache Airflow, with Docker Compose used for containerized orchestration.

---

## 🛠️ Tech Stack

| Tool              | Purpose                                      |
|-------------------|----------------------------------------------|
| Apache Kafka       | Real-time message ingestion (Producer & Topic) |
| Apache Spark       | Structured Streaming for data transformation |
| PostgreSQL         | Persistent data storage                      |
| Apache Airflow     | Orchestration and job scheduling             |
| Docker Compose     | Multi-container orchestration                |
| Jupyter Notebook   | Exploratory data analysis & visualization    |

---

## 📌 Architecture

1. A Kafka Producer reads data from NYC taxi CSV files and streams trip records into a Kafka topic.
2. Spark Structured Streaming consumes the data from Kafka, processes and transforms it.
3. The cleaned and structured data is loaded into a PostgreSQL database.
4. Apache Airflow manages and schedules the entire pipeline as a Directed Acyclic Graph (DAG).
5. Data is then queried and visualized using Jupyter Notebooks.

---

## 📁 Project Structure

nyc-taxi-data-engineering-pipeline/
├── kafka-producer/ # Kafka data producer script
├── kafka-consumer/ # Optional consumer for testing/debugging
├── spark-job/ # Spark ETL logic using Structured Streaming
├── db/ # PostgreSQL initialization or schema
├── airflow/dags/ # Airflow DAGs to automate pipeline
├── notebooks/ # Jupyter Notebooks for data exploration
├── docker-compose.yml # Service orchestration
└── README.md # Project documentation

Key Highlights

Real-time ingestion of high-volume NYC Taxi trip data.
Stream processing with fault-tolerant and scalable Spark jobs.
Data persistence with PostgreSQL for downstream querying.
Seamless workflow management with Airflow DAGs.
Local development using Docker Compose for complete isolation.
📎 Connect With Me

If you found this project insightful, feel free to ⭐ the repo and connect with me on LinkedIn! - https://www.linkedin.com/in/sarvesh-jere/
