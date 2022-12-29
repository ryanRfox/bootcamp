FROM mcr.microsoft.com/devcontainers/python:0-3.11

ENV PYTHONUNBUFFERED 1

RUN pip3 --disable-pip-version-check --no-cache-dir install beaker-pyteal

RUN cd ~/ && git clone https://github.com/algorand/sandbox

RUN cd ~/sandbox && ./sandbox up dev -v && ./sandbox stop



# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



