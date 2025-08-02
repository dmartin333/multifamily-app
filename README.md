# Multifamily Underwriting SaaS

A comprehensive SaaS platform for multifamily real estate underwriting and analysis, built with modern technologies and enterprise-grade architecture.

## 🏗️ Architecture Overview

- **Backend**: Python/FastAPI with modular design
- **Frontend**: React/TypeScript with Tailwind CSS
- **Infrastructure**: Docker containerization with CI/CD pipeline
- **Monitoring**: Prometheus metrics and health checks
- **Documentation**: OpenAPI/Swagger with interactive docs

## 📁 Project Structure

```
multifamily_acquisitions_automator/
├── src/
│   ├── backend/
│   │   ├── auth/                 # Authentication & Authorization
│   │   ├── collaboration/        # Comments & Team Features
│   │   ├── docs/                 # API Documentation
│   │   ├── etl/                  # Data Ingestion & Parsing
│   │   ├── integrations/         # External API Connectors
│   │   ├── monitoring/           # Performance & Metrics
│   │   ├── reporting/            # Export & Report Generation
│   │   └── underwriting/         # Core Business Logic
│   └── frontend/
│       ├── components/           # Reusable UI Components
│       ├── i18n/                 # Internationalization
│       └── pages/                # Route Components
├── data/                         # Application Data
│   └── assumptions/              # Underwriting Assumption Sets
├── templates/report/             # Report Templates
├── tests/                        # Comprehensive Test Suite
├── .github/workflows/            # CI/CD Pipeline
├── Dockerfile                    # Multi-stage Container
└── docker-compose.yml           # Service Orchestration
```

## 🚀 Core Features

### **Financial Analysis** ✅
- ✅ Pro-forma modeling and analysis
- ✅ Scenario comparison and sensitivity testing
- ✅ IRR, NPV, and cash flow calculations
- ✅ Assumption management and validation

### **Data Management** ✅
- ✅ Multi-format file import (CSV, XLSX, PDF)
- ✅ External data source integration (CoStar, Yardi, BLS, Salesforce)
- ✅ Real-time data synchronization
- ✅ Data validation and quality checks

### **Reporting & Export** ✅
- ✅ Excel export with openpyxl (XLSX format)
- ✅ PDF export (WeasyPrint/Puppeteer ready)
- ✅ PowerPoint export (python-pptx ready)
- ✅ Customizable report templates

### **Team Collaboration** ✅
- ✅ Real-time commenting and annotations
- ✅ Model sharing and version control
- ✅ Team-based access controls
- ✅ Activity tracking and audit trails

### **Enterprise Features** ✅
- ✅ OAuth2 and SAML authentication
- ✅ Role-based permissions
- ✅ Audit logging and compliance
- ✅ Scalable microservices architecture

## 🛠️ Technology Stack

### **Backend**
- **Framework**: FastAPI (Python 3.11)
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Authentication**: OAuth2, SAML
- **Monitoring**: Prometheus, custom metrics
- **Testing**: pytest with coverage

### **Frontend**
- **Framework**: React 18 with TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Hooks
- **Internationalization**: i18next
- **Testing**: Jest, React Testing Library

### **Infrastructure**
- **Containerization**: Docker multi-stage builds
- **Orchestration**: Docker Compose
- **CI/CD**: GitHub Actions
- **Documentation**: OpenAPI/Swagger
- **Monitoring**: Health checks, metrics endpoints

## 🚀 Quick Start

### **Prerequisites**
- Docker and Docker Compose
- Node.js 18+ (for development)
- Python 3.11+ (for development)

### **Development Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/dmartin333/multifamily-app.git
   cd multifamily-app
   ```

2. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Metrics: http://localhost:8000/metrics

### **Local Development**

1. **Backend Setup**
   ```bash
   cd src/backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

2. **Frontend Setup**
   ```bash
   cd src/frontend
   npm install
   npm start
   ```

## 📊 API Documentation

The API is fully documented with OpenAPI/Swagger:

- **Interactive Docs**: `/docs` - Swagger UI
- **API Schema**: `/openapi.json` - OpenAPI specification
- **Alternative Docs**: `/redoc` - ReDoc interface

### **Key Endpoints**

- `POST /scenarios/` - Create underwriting scenarios
- `POST /scenarios/clone/` - Clone existing scenarios
- `GET /scenarios/{base_id}/compare/{alt_id}/` - Compare two scenarios
- `POST /comments/` - Add collaboration comments
- `GET /metrics` - Prometheus metrics
- `GET /health` - Health check

## 🧪 Testing

### **Backend Tests**
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### **Frontend Tests**
```bash
# Run tests
npm test

# Run linting
npm run lint
```

### **CI/CD Pipeline**
The project includes automated testing via GitHub Actions:
- Runs on every push to `main` branch
- Tests both frontend (npm ci, lint, test) and backend (pip install, pytest)
- Fails the job if any step errors

## 📈 Monitoring & Observability

### **Metrics**
- Request counts and latency
- Business metrics (models, scenarios, reports)
- Error rates and availability
- Custom underwriting metrics

### **Health Checks**
- Service health monitoring
- Database connectivity
- External API status
- System resource utilization

## 🔧 Configuration

### **Environment Variables**
```bash
# Database
DATABASE_URL=postgresql://postgres:password@db:5432/multifamily_underwriting

# Redis
REDIS_URL=redis://redis:6379

# Environment
ENVIRONMENT=production

# External APIs
COSTAR_API_KEY=your_costar_key
YARDI_API_KEY=your_yardi_key
BLS_API_KEY=your_bls_key
SALESFORCE_API_KEY=your_salesforce_key
```

### **Assumption Sets**
The platform includes pre-configured assumption sets in `data/assumptions/`:
- **Conservative**: Risk-averse underwriting assumptions
- **Moderate**: Balanced risk-return profiles
- **Aggressive**: Growth-oriented assumptions

### **Docker Configuration**
- Multi-stage builds for optimization
- Health checks for all services
- Volume persistence for data
- Network isolation

## 🚀 Deployment

### **Production Deployment**
```bash
# Build and deploy
docker-compose -f docker-compose.prod.yml up -d

# Scale services
docker-compose up -d --scale app=3
```

### **CI/CD Pipeline**
- Automated testing on push to main
- Code quality checks
- Security scanning
- Automated deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### **Development Guidelines**
- Follow PEP 8 for Python code
- Use TypeScript for frontend components
- Write comprehensive tests
- Update documentation for new features

## 📋 Roadmap

### **Phase 1: Core Platform** ✅
- [x] Basic underwriting engine
- [x] Data import capabilities
- [x] Reporting system (XLSX export)
- [x] External API integrations (CoStar, BLS, Salesforce, Yardi)
- [x] Assumption management system
- [x] Scenario comparison and cloning
- [x] CI/CD pipeline
- [x] User authentication
- [x] Team collaboration

### **Phase 2: Advanced Features** 🚧
- [ ] Machine learning models
- [ ] Advanced analytics
- [ ] Mobile application
- [ ] Enhanced third-party integrations
- [ ] Advanced reporting (PDF, PowerPoint)
- [ ] Real-time collaboration features

### **Phase 3: Enterprise Features** 📋
- [ ] Multi-tenant architecture
- [ ] Advanced security features
- [ ] Compliance reporting
- [ ] API marketplace
- [ ] White-label solutions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [API Docs](http://localhost:8000/docs)
- **Issues**: [GitHub Issues](https://github.com/dmartin333/multifamily-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/dmartin333/multifamily-app/discussions)

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- React team for the frontend framework
- Docker for containerization
- The open-source community for various libraries and tools

---

**Built with ❤️ for the real estate industry** 