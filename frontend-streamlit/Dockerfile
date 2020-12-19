FROM continuumio/miniconda3

WORKDIR /app

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

COPY ald-api-streamlit.yaml .
RUN conda env create --file ald-api-streamlit.yaml

COPY . .

EXPOSE 8080

CMD ["conda", "run", "-n", "ald-api-streamlit", "streamlit", "run", "main.py", "--server.port", "8080"]
