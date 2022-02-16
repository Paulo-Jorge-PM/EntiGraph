#!/bin/bash


RABBITMQ_PATH="./rabbitMQ/run.sh"


echo "RABBITMQ at: http://localhost:15672"

gnome-terminal --tab --title="RABBITMQ" -- "$RABBITMQ_PATH"
echo "RABBITMQ_PATH = DONE"

exec bash
