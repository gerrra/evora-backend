# Evora Backend

FastAPI backend service for Evora Orchestrator.

## Local Development

### Prerequisites

- Python 3.11+
- PostgreSQL (optional for full functionality)
- Redis (optional for full functionality)

### Setup

1. Clone the repository and navigate to the backend directory:
   ```bash
   cd evora-backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Copy environment variables:
   ```bash
   cp .env.example .env
   ```

5. Edit `.env` file with your configuration values.

### Running the Application

Start the development server:
```bash
python -m uvicorn app.main:app --reload
```

Or use the script:
```bash
python -m dev
```

The API will be available at `http://localhost:8000`

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

Run tests:
```bash
python -m test
```

Or with pytest directly:
```bash
pytest
```

## Code Quality

### Formatting
```bash
python -m format
```

### Linting
```bash
python -m lint
```

## Environment Variables

See `.env.example` for required environment variables:

- `POSTGRES_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string  
- `S3_ENDPOINT`: S3-compatible storage endpoint
- `STRIPE_PUBLIC_KEY`: Stripe public key
- `STRIPE_SECRET_KEY`: Stripe secret key
- `JWT_SECRET`: JWT signing secret
