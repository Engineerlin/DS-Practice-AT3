FROM python:3.8.2

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py"]
