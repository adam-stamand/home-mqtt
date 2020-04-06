FROM python:3


ARG client


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/clients/common common/
COPY src/clients/${client} ${client}/


RUN ln -s ${client}/main.py entrypoint
CMD [ "python", "entrypoint" ]