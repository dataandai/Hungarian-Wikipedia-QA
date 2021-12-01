FROM ubuntu:latest 
RUN apt-get update && apt-get install -y python3.8 python3.8-dev python3-pip && rm -rf /var/lib/apt/lists/*
ADD  hu_core_ud_lg-0.3.1  /app
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN pip3 install -r requirements.txt --find-links https://download.pytorch.org/whl/torch_stable.html


EXPOSE 8000
ENTRYPOINT [ "python3.8" ]
CMD ["api.py"]
