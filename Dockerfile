FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y wget

WORKDIR /tmp

RUN wget -O agate.gz https://github.com/mbrubeck/agate/releases/download/v2.3.0/agate.x86_64-unknown-linux-gnu.gz \
    && gunzip agate.gz \
    && mkdir -p /opt/bin \
    && mv agate /opt/bin \
    && chmod a+x /opt/bin/agate

RUN useradd agate

USER agate

WORKDIR /var/gemini

CMD /opt/bin/agate \
    --content ./data \
    --key ./key.rsa \
    --cert ./cert.pem \
    --addr 0.0.0.0:1965 \
    --hostname gem.recursive.one \
    --lang en-US
