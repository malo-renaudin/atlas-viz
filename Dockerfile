FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir streamlit numpy matplotlib nilearn
EXPOSE 8501
CMD ["streamlit", "run", "atlas_app.py", "--server.port=8501", "--server.address=0.0.0.0"]