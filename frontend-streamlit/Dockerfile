FROM continuumio/miniconda3

WORKDIR /app

COPY ald-api-streamlit.yaml .
RUN conda env create --file ald-api-streamlit.yaml

COPY . .

EXPOSE 8080

CMD ["conda", "run", "-n", "ald-api-streamlit", "streamlit", "run", "main.py"]