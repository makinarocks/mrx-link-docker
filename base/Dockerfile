ARG BASE_IMAGE="python:3.9-buster"
FROM ${BASE_IMAGE}

LABEL maintainer="Hwiyeon Cho <hwiyeon.cho@makinarocks.ai>"

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    bzip2 \
    ca-certificates \
    curl \
    fonts-liberation \
    git \
    git-lfs \
    locales \
    sudo \
    tini \
    vim \
    wget \
    xz-utils \
    zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

ENV HOME="/root"
ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US.UTF-8"
ENV LC_ALL="en_US.UTF-8"
ENV NODE_PREFIX="/opt/nodejs"
ENV PATH="${NODE_PREFIX}/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV SHELL="/bin/bash"

# Install NodeJS.
ARG NODEJS_VERSION="v18.10.0"
WORKDIR /tmp
RUN export ARCH= && \
    dpkgArch="$(dpkg --print-architecture)" && \
    case "${dpkgArch##*-}" in \
    amd64) export ARCH="x64";; \
    arm64) export ARCH="arm64";; \
    *) echo "unsupported architecture"; exit 1 ;; \
    esac && \
    declare nodejs_mirror="https://nodejs.org/dist/${NODEJS_VERSION}" && \
    declare nodejs_release="node-${NODEJS_VERSION}-linux-${ARCH}" && \
    declare nodejs_tar="${nodejs_release}.tar.xz" && \
    wget "${nodejs_mirror}/${nodejs_tar}" -O "${nodejs_tar}" && \
    tar -xJf "${nodejs_tar}" && \
    mv "${nodejs_release}" "${NODE_PREFIX}" && \
    ln -s "${NODE_PREFIX}/bin/node" /usr/local/bin/node && \
    ln -s "${NODE_PREFIX}/bin/npm" /usr/local/bin/npm && \
    ln -s "${NODE_PREFIX}/bin/npx" /usr/local/bin/npx && \
    /usr/local/bin/npm install --global yarn && \
    /usr/local/bin/npm cache clean --force && \
    rm "${nodejs_tar}"

# Install Python requirements.
WORKDIR /tmp
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r /tmp/requirements.txt && \
    rm -fr "$(python3 -m pip cache dir)"

WORKDIR /workspace

ENTRYPOINT [ "/usr/bin/tini", "-g", "--" ]
CMD [ "sh", "-c", "python3" ]
