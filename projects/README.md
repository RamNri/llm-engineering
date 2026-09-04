# AI Company Brochure Generator

## Problem

Company information is often distributed across multiple pages
such as About, Products, Careers, and Company pages.

This application uses an LLM pipeline to identify relevant pages
and generate a concise company brochure.

## Architecture

Website
↓
Web Scraper
↓
Link Extraction
↓
LLM Link Selection
↓
Relevant Page Retrieval
↓
LLM Brochure Generation

## Technologies

- Python
- OpenAI API
- BeautifulSoup
- Requests
- Structured JSON Output

## Key Engineering Concepts

- Multi-step LLM pipelines
- Model selection
- Structured outputs
- Web scraping
- Prompt engineering

## Status

Learning implementation. Further improvements planned.