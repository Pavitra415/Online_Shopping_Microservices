# Online_Shopping_Microservices
# Online Shopping Microservices

## Aim

To develop an Online Shopping application using microservices and analyze its performance using Docker and workload testing.

## Microservices

The project contains three microservices:

- **Product Service** – Port 5000
- **User Service** – Port 5001
- **Order Service** – Port 5002

## Architecture

```text
                 Client
                    |
                    v
             Order Service
                Port 5002
                /       \
               /         \
              v           v
     Product Service   User Service
        Port 5000        Port 5001
```
## Technologies Used
- Python
- Flask
- REST API
- Docker
- Docker Compose
- Requests
## Project Structure

```text
OnlineShoppingMicroservices/
│
├── product-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── user-services/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── order-services/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── Outputs/
│   ├── 1_response_time.png
│   ├── 2_throughput.png
│   ├── 3_cpu_utilization.png
│   └── 4_memory_usage.png
│
├── docker-compose.yml
├── load_test.py
└── README.md
```
## Product Service

Manages product information.



```text
GET /products
GET /products/<id>
GET /health
```

**Port:** `5000`

---

## User Service

Manages user information.



```text
GET /users
GET /users/<id>
GET /health
```

**Port:** `5001`

---

## Order Service

Creates orders and communicates with the Product and User Services.



```text
POST /orders
GET /orders
GET /health
```

**Port:** `5002`

---
## Dockerization

### Build Docker Images

```cmd
docker compose build
```

### Start the Services

```cmd
docker compose up -d
```

### Check Running Containers

```cmd
docker ps
```
## Inter-Service Communication

The Order Service communicates with both Product Service and User Service.

```text
Order Service
     |
     +----> Product Service
     |
     +----> User Service
```

### Test an Order

```cmd
curl -X POST http://127.0.0.1:5002/orders -H "Content-Type: application/json" -d "{\"user_id\":1,\"product_id\":1,\"quantity\":2}"
```

### Result

The order is successfully created after the Order Service communicates with the Product Service and User Service.
## Workload Testing

Five workload levels were tested with different concurrency levels. Each workload used 500 requests.

![Workload Results](Outputs/workload.png)

### Overall Result

- **Total Requests:** 2500
- **Successful Requests:** 2500
- **Failed Requests:** 0
- **Maximum Throughput:** 302.69 req/s
- **Highest Response Time:** 0.0517 s
## Performance Graphs

### 1. Concurrent Requests vs Response Time

![Response Time](Outputs/1_response_time.png)

### 2. Concurrent Requests vs Throughput

![Throughput](Outputs/2_throughput.png)

### 3. Concurrent Requests vs CPU Utilization

![CPU Utilization](Outputs/3_cpu_utilization.png)

### 4. Concurrent Requests vs Memory Usage

![Memory Usage](Outputs/4_memory_usage.png)
## Performance Analysis
- Throughput increased as concurrency increased.
- Response time increased at higher workload levels.
- No requests failed during testing.
- Order Service was the relatively resource-heavy service.
- At higher concurrency, throughput improvement became smaller.
## Conclusion
The Online Shopping microservices application was successfully developed, Dockerized, deployed, and tested. The three microservices communicated successfully through REST APIs, and all **2,500 workload requests were completed successfully with zero failures**. The performance analysis showed that increasing concurrency improved system throughput, while response time increased at higher workload levels. Overall, the experiment demonstrated the successful implementation, deployment, and performance evaluation of a microservices-based application.
