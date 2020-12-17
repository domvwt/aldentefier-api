FROM continuumio/miniconda3

WORKDIR /app

COPY ald-api-backend.yaml .
RUN conda env create --file ald-api-backend.yaml

COPY . .

EXPOSE 8080

CMD ["conda", "run", "-n", "ald-api-backend", "python", "main.py"]