# Stock Anomaly Detection System

A real-time data pipeline for e-commerce event streaming and analytics using Apache Kafka and Apache Druid. This system processes synthetic e-commerce data to demonstrate streaming analytics capabilities.

## System Architecture

```
[Data Generator] -> [Kafka Cluster] -> [Apache Druid] -> [Analytics Queries]
```

### Components
- **Data Generator**: Python script generating synthetic e-commerce events
- **Apache Kafka**: Distributed streaming platform (2 controllers, 2 brokers)
- **Apache Druid**: Real-time analytics database
- **PostgreSQL**: Metadata storage for Druid

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- Required Python packages:
  ```bash
  pip install faker kafka-python
  ```

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Stock-Anomaly_Detection.git
   cd Stock-Anomaly_Detection
   ```

2. **Start the infrastructure**
   ```bash
   docker compose up -d
   ```

3. **Run the data generator**
   ```bash
   python main.py
   ```

## Service Endpoints

- **Druid Console**: http://localhost:8888
- **Kafka Brokers**: 
  - localhost:29092
  - localhost:39092
- **PostgreSQL**: localhost:5432
- **Zookeeper**: localhost:2181

## Data Schema

The system processes e-commerce events with the following structure:

```json
{
    "user_id": "integer",
    "event_type": "string (click|view|purchase)",
    "country": "string",
    "city": "string",
    "device": "string (mobile|desktop|tablet)",
    "product_id": "integer",
    "price": "float",
    "quantity": "integer",
    "timestamp": "unix_timestamp"
}
```

## Analytics Capabilities

Example queries available in [`druid.sql`](druid.sql):

1. Device-based analytics
   - Total sales by device type
   - Average price per device

2. Geographic analysis
   - Unique users per country
   - Event distribution by location

3. Product metrics
   - Top selling products
   - Revenue by product

4. Time-based analysis
   - Minute-by-minute event tracking
   - Sales trends over time

## Project Structure

```
├── docker-compose.yml    # Service orchestration
├── main.py              # Data generator
├── druid.sql            # Example queries
└── environment          # Druid configuration
```

## Configuration

The system uses multiple containerized services:
- 2 Kafka Controllers
- 2 Kafka Brokers
- Complete Druid stack (Coordinator, Broker, Historical, MiddleManager, Router)
- Zookeeper for coordination
- PostgreSQL for metadata storage

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Apache Kafka
- Apache Druid
- Python Faker library

## Support

For support, please open an issue in the GitHub repository.