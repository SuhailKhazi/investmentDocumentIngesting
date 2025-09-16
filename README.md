# Alternative Investments Document Intelligence — Prototype

## Overview
This prototype demonstrates an AI-native pipeline for financial institutions to process unstructured alternative-investment documents (Capital Calls & Distribution notices).  

**Pipeline flow:**  
PDF ingest → OCR & classification → field extraction & normalization → store in Postgres → query via API/UI → human-in-the-loop review.

## Architecture (high-level)
- **Ingress/API:** FastAPI service for uploading PDFs & querying results.  
- **Message Broker:** Redis + RQ for job orchestration.  
- **Preprocessing & OCR:** Python worker using PyMuPDF + Tesseract.  
- **Classifier & Extractor:** ML (HuggingFace/LayoutLM-lite) + regex fallback.  
- **Database:** Postgres for normalized records, audit trail.  
- **Storage:** MinIO (S3-compatible) for raw PDFs & OCR artifacts.  
- **UI:** Simple React/Streamlit app for review.  
- **Observability:** Logs + metrics (Prometheus/Grafana in production).  

## Key Features
- Document classification (Capital Call, Distribution)  
- Field extraction (Fund ID, LP ID, Dates, Amounts, Currency, Type)  
- Normalization of dates/currency/numbers  
- Human-in-the-loop correction UI  
- REST API to ingest, check status, search, and review documents  

## Quick Start
```bash
# Start services
docker-compose up -d

# Upload a PDF
curl -F "file=@sample_call.pdf" http://localhost:8000/ingest

# Check status
curl http://localhost:8000/status/1

# View results in UI
open http://localhost:3000
