FROM python:3.12.3-bookworm

WORKDIR /project

COPY . .

RUN apt update && apt dist-upgrade -y
RUN pip install -U wheel
RUN pip install -U nltk pandas Unidecode num2words pyarrow numpy ipykernel
RUN pip install streamlit

ENTRYPOINT [ "top", "-b" ]