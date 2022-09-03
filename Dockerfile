FROM python:3.7.13-buster
RUN apt-get update && apt-get install -y \
  locales \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN sed -i -E 's/# (ja_JP.UTF-8)/\1/' /etc/locale.gen \
  && locale-gen
ENV LANG ja_JP.UTF-8
WORKDIR /FakerRealText
RUN pip install -U pip
RUN pip install mecab-python3
RUN pip install unidic-lite
RUN pip install memory-profiler