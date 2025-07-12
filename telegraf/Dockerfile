FROM telegraf:1.30


RUN apt-get update
RUN apt install -y netcat-openbsd

COPY wait-for-kafka.sh /wait-for-kafka.sh
RUN chmod +x /wait-for-kafka.sh
ENTRYPOINT ["/wait-for-kafka.sh"]


RUN apt-get install -y --no-install-recommends postgresql-client && \
    rm -rf /var/lib/apt/lists/*