# Student Score Prediction API 🎓

A FastAPI-based machine learning service that predicts student assessment scores based on their learning characteristics. The API uses a trained ML model to predict student performance based on comprehension, attention, focus, retention, and engagement time metrics.

## 🚀 Live Demo

**API Base URL:** [https://student-backend-2919.onrender.com](https://student-backend-2919.onrender.com)

**API Documentation:** [https://student-backend-2919.onrender.com/docs](https://student-backend-2919.onrender.com/docs)

## 📋 Features

- **Machine Learning Predictions**: Predict student assessment scores using trained ML models
- **Batch Processing**: Support for predicting multiple students (up to 200) in a single request
- **Authentication & Authorization**: JWT-based authentication with API key validation
- **Caching**: Redis-based caching for improved performance
- **Monitoring**: Prometheus metrics integration for monitoring API performance
- **Logging**: Comprehensive logging middleware for request tracking
- **Containerized**: Docker and Docker Compose support for easy deployment

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.110.0
- **ML Libraries**: scikit-learn 1.3.2, pandas 2.0.3, numpy 1.26.4
- **Authentication**: python-jose 3.3.0 (JWT tokens)
- **Caching**: Redis 5.0.4
- **Monitoring**: Prometheus + Grafana
- **Deployment**: Docker, Docker Compose
- **Server**: Uvicorn

## 📊 API Endpoints

### Authentication
- `POST /login` - Authenticate and get JWT token

### Predictions
- `POST /predict` - Predict student score (single or batch)

### Monitoring
- `/metrics` - Prometheus metrics endpoint

## 🔧 Installation & Setup

### Prerequisites
- Python 3.10+
- Docker & Docker Compose (optional)
- Redis (if running locally)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd student-backend
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   # Create .env file
   API_KEY=your-api-key
   JWT_SECRET_KEY=your-secret-key
   REDIS_URL=redis://localhost:6379
   ```

4. **Start Redis (if running locally)**
   ```bash
   redis-server
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Docker Deployment

1. **Using Docker Compose (Recommended)**
   ```bash
   docker-compose up -d
   ```

   This will start:
   - FastAPI application on port 8000
   - Redis on port 6379
   - Prometheus on port 9090
   - Grafana on port 3000

2. **Using Docker only**
   ```bash
   docker build -t student-backend .
   docker run -p 8000:8000 student-backend
   ```

## 📝 API Usage

### 1. Authentication

First, get an authentication token:

```bash
curl -X POST "https://student-backend-2919.onrender.com/login" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "admin",
       "password": "admin"
     }'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 2. Single Student Prediction

```bash
curl -X POST "https://student-backend-2919.onrender.com/predict" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "X-API-Key: demo-key" \
     -d '{
       "comprehension": 75.5,
       "attention": 82.3,
       "focus": 78.9,
       "retention": 80.1,
       "engagement_time": 95
     }'
```

Response:
```json
{
  "predicted_score": "78.45"
}
```

### 3. Batch Student Prediction

```bash
curl -X POST "https://student-backend-2919.onrender.com/predict" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "X-API-Key: demo-key" \
     -d '{
       "students": [
         {
           "comprehension": 75.5,
           "attention": 82.3,
           "focus": 78.9,
           "retention": 80.1,
           "engagement_time": 95
         },
         {
           "comprehension": 68.2,
           "attention": 74.8,
           "focus": 71.3,
           "retention": 72.5,
           "engagement_time": 87
         }
       ]
     }'
```

Response:
```json
{
  "batch_size": 2,
  "predictions": [
    {"predicted_score": "78.45"},
    {"predicted_score": "71.23"}
  ]
}
```

## 📊 Input Parameters

The API expects the following student characteristics:

| Parameter | Type | Description | Range |
|-----------|------|-------------|-------|
| `comprehension` | float | Student's comprehension level | 0-100 |
| `attention` | float | Student's attention span | 0-100 |
| `focus` | float | Student's focus ability | 0-100 |
| `retention` | float | Student's retention capacity | 0-100 |
| `engagement_time` | integer | Time spent engaged (minutes) | 0+ |

## 🔒 Security

- **JWT Authentication**: All prediction endpoints require valid JWT tokens
- **API Key Validation**: Additional API key validation for enhanced security
- **Rate Limiting**: Built-in protection against abuse
- **Input Validation**: Comprehensive input validation using Pydantic models

## 📈 Monitoring & Observability

### Prometheus Metrics
Access metrics at: `https://student-backend-2919.onrender.com/metrics`

### Grafana Dashboard
- Local: http://localhost:3000 (when using Docker Compose)
- Default credentials: admin/admin

### Logging
The application includes comprehensive logging middleware that tracks:
- Request/response times
- API usage patterns
- Error rates
- Cache hit/miss ratios

## 🗂️ Project Structure

```
student-backend/
├── app/
│   ├── api/
│   │   ├── routes_auth.py      # Authentication endpoints
│   │   └── routes_predict.py   # Prediction endpoints
│   ├── cache/
│   │   └── redis_cache.py      # Redis caching logic
│   ├── core/
│   │   ├── config.py           # Application configuration
│   │   ├── dependencies.py     # Dependency injection
│   │   ├── exceptions.py       # Exception handlers
│   │   └── security.py         # JWT and security utilities
│   ├── middleware/
│   │   └── logging_middleware.py # Request logging
│   ├── models/
│   │   └── model.joblib        # Trained ML model
│   ├── services/
│   │   └── model_service.py    # ML prediction logic
│   └── main.py                 # FastAPI application entry point
├── data/
│   ├── student_performance.csv # Raw data
│   └── students_cleaned.csv    # Processed data
├── notebooks/
│   ├── analysis.ipynb          # Data analysis
│   ├── assignment_score.ipynb  # Score analysis
│   └── synthetic_data.ipynb    # Data generation
├── training/
│   ├── train_model.py          # Model training script
│   └── train_utils.py          # Training utilities
├── docker-compose.yml          # Multi-service setup
├── Dockerfile                  # Container definition
├── requirements.txt            # Python dependencies
└── prometheus.yml              # Prometheus configuration
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the API documentation at `/docs` endpoint
- Review the monitoring dashboards for system health

## 🔄 Version History

- **v1.0.0** - Initial release with basic prediction functionality
- **v1.1.0** - Added batch prediction support
- **v1.2.0** - Implemented caching and monitoring
- **v1.3.0** - Enhanced security and authentication

---

**Built with ❤️ using FastAPI and scikit-learn**
