# Use an official Ubuntu base image
FROM kalilinux/kali-rolling

WORKDIR /code

COPY . /code
# Update the package lists
RUN apt-get update

# Install system packages
RUN apt-get install -y grep git python3 python3-pip coreutils curl

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of your application files

RUN curl -O https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin

EXPOSE 7860

CMD ["streamlit", "run", "app.py","--server.port", "7860"]

