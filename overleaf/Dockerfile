FROM docker.io/ubuntu:noble

RUN apt update && apt install -y git curl

RUN curl -sSL https://get.docker.com/ | sh
RUN git clone https://github.com/overleaf/toolkit.git /overleaf-toolkit

RUN /overleaf-toolkit/bin/init
CMD ["/overleaf-toolkit/bin/up"]