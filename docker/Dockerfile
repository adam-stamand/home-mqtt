FROM python:3


ARG client


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src src
COPY util util
COPY conf conf
COPY main.py main.py



RUN ln -s main.py entrypoint
CMD [ "python", "entrypoint" ]