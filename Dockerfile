FROM python:3.7-alpine
RUN apk add alpine-sdk
RUN pip install discord
COPY bot.py /bot.py
ENTRYPOINT [ "/usr/local/bin/python3", "/bot.py" ]