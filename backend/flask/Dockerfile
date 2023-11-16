#--platform=$BUILDPLATFORM
FROM  python:3.10-alpine AS flaskBuilder

WORKDIR /app
COPY requirements.txt /app/

#  cache dependencies , resuing if is not changed 
# RUN --mount=type=cache,target=/root/.cache/pip \ 
#     pip3 install -r requirements.txt

RUN  pip3 install -r requirements.txt


COPY server /app/


ENV PYTHONPATH=/app/

CMD ["python3", "server.py"]
