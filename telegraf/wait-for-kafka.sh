#!/bin/bash

echo "Esperando o Kafka ficar disponível..."
while ! nc -z kafka 9092; do
  sleep 1
done

echo "Kafka está disponível, iniciando Telegraf..."
exec telegraf
