# nyc-taxi-data-engineering-pipeline
So it is very important to know some topics before we dive into the project.
You should first be familiar with microservices. So microservies is an architecture where we run all the services or systems differently and as an independant component. So basically each application process is run as a service independantly. These services communicate with each other using lightweight APIs. Services are built for business capabilities and each service performs an unique function which makes them easier to deploy. 

# NYC Taxi Data Engineering Pipeline 

##  Overview
This project builds a **real-time data pipeline** for NYC taxi trip data using modern data engineering tools. It simulates real-world ingestion, processing, and orchestration to showcase data streaming and batch analytics capabilities.

##  Tools Used
- **Apache Kafka** – real-time data ingestion
- **Apache Spark Structured Streaming** – ETL and transformation
- **PostgreSQL** – data storage
- **Apache Airflow** – orchestration and scheduling
- **Docker + Docker Compose** – containerized setup
- **Jupyter Notebook** – exploratory analysis and visualization

##  Architecture


1. **Kafka Producer** reads CSV and pushes trip data to a Kafka topic.
2. **Spark Streaming Job** consumes from Kafka, transforms the data, and loads into PostgreSQL.
3. **Airflow DAG** schedules and monitors the entire flow.
4. **Notebook** connects to PostgreSQL for visual exploration.

## 🗂 Project Structure

nyc-taxi-data-engineering-pipeline/
├── kafka-producer/ # Kafka ingestion script
├── spark-job/ # Spark ETL logic
├── airflow/dags/ # Airflow DAG to schedule the flow
├── db/ # DB schema
├── notebooks/ # Visualizations
├── docker-compose.yml # All-in-one orchestrator
├── README.md # You're here!
