FROM python:3.8-slim-buster
COPY . /work
WORKDIR /work
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENTRYPOINT [ "python" ]
CMD ["./1.py"]