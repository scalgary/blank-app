FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

WORKDIR /workspace

# Install system packages if packages.txt exists
COPY packages.txt* ./
RUN if [ -f packages.txt ]; then \
    apt update && apt upgrade -y && \
    xargs apt install -y < packages.txt; \
    fi

# Install Python requirements
COPY requirements.txt* ./
RUN if [ -f requirements.txt ]; then \
    pip3 install -r requirements.txt; \
    fi && \
    pip3 install streamlit

# Copy application files
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false", "--server.address", "0.0.0.0"]