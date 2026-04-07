#!/usr/bin/env sh
while true; do
  date >> /shared/heartbeat.log
  sleep 10
done
