ARG BASE_IMAGE="ghcr.io/makinarocks/mrx-link-base:python3.9"
FROM ${BASE_IMAGE}

LABEL maintainer="Hwiyeon Cho <hwiyeon.cho@makinarocks.ai>"

USER root

COPY fix-permissions.sh /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

RUN sed -i "s/^#force_color_prompt=yes/force_color_prompt=yes/" /etc/skel/.bashrc && \
    echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    sed -i.bak -e "s/^%admin/#%admin/" /etc/sudoers && \
    sed -i.bak -e "s/^%sudo/#%sudo/" /etc/sudoers

ARG MRX_LINK_VERSION="0.10.4"
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade "build>=0.7" "setuptools>=61.0,<64.0" "wheel>=0.37" && \
    python3 -m pip install --upgrade "mrx-link==${MRX_LINK_VERSION}" && \
    python3 -c "import mrx_link" && \
    rm -fr "$(python3 -m pip cache dir)"

ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

ENV HOME="/home/${NB_USER}"
ENV NB_PREFIX="/"
ENV NB_UID="${NB_UID}"
ENV NB_GID="${NB_GID}"
ENV NB_USER="${NB_USER}"

RUN adduser --home "${HOME}" --shell "${SHELL}" --uid "${NB_UID}" --gid "${NB_GID}" --disabled-password "${NB_USER}" && \
    chmod g+w /etc/passwd && \
    echo "${NB_USER} ALL=(ALL) NOPASSWD:/usr/bin/apt,/usr/bin/apt-get" >> /etc/sudoers && \
    chown -R "${NB_UID}:${NB_GID}" "${HOME}" && \
    fix-permissions "${HOME}"

RUN chown -R "${NB_UID}:${NB_GID}" "/opt" && \
    fix-permissions "/opt"

WORKDIR "${HOME}/.jupyter"
COPY jupyter_lab_config.py "${HOME}/.jupyter/jupyter_lab_config.py"
RUN chown -R "${NB_UID}:${NB_GID}" "${HOME}/.jupyter" && \
    fix-permissions "${HOME}/.jupyter"

WORKDIR "${HOME}/workspace"
RUN chown -R "${NB_UID}:${NB_GID}" "${HOME}/workspace" && \
    fix-permissions "${HOME}/workspace"

USER ${NB_USER}

WORKDIR "${HOME}/workspace"

EXPOSE 8888

ENTRYPOINT [ "/usr/bin/tini", "-g", "--" ]
CMD [ "sh", "-c", "python3 -m jupyterlab --config=${HOME}/.jupyter/jupyter_lab_config.py" ]
