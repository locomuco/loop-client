# derived from https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/installation/installing.html
FROM ubuntu:22.04 as base

ENV DEBIAN_FRONTEND=noninteractive
ENV NCS_PATH=/opt/ncs

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git cmake ninja-build gperf ccache dfu-util device-tree-compiler wget \
    python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file \
    make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1 unzip

# install CMake
RUN cd ${HOME} && \
    wget https://apt.kitware.com/kitware-archive.sh && \
    bash kitware-archive.sh

# install GN tool
RUN mkdir ${HOME}/gn && cd ${HOME}/gn && \
    wget -O gn.zip https://chrome-infra-packages.appspot.com/dl/gn/gn/linux-amd64/+/latest && \
    unzip gn.zip && \
    rm gn.zip && \
    export PATH=${HOME}/gn:"$PATH"

# install West
RUN pip3 install west && \
    export PATH=~/.local/bin:"$PATH"

# checkout NCS
RUN mkdir $NCS_PATH && cd $NCS_PATH && \
    west init -m https://github.com/nrfconnect/sdk-nrf --mr v2.4.2 && \
    west update && \
    west zephyr-export

# install NCS requirements
RUN pip install -r $NCS_PATH/zephyr/scripts/requirements.txt && \
    pip install -r $NCS_PATH/nrf/scripts/requirements.txt && \
    pip install -r $NCS_PATH/bootloader/mcuboot/scripts/requirements.txt

# install toolchain
RUN cd /opt && \
    wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.1/zephyr-sdk-0.16.1_linux-x86_64.tar.xz && \
    tar xvf zephyr-sdk-0.16.1_linux-x86_64.tar.xz && \
    cd zephyr-sdk-0.16.1 && \
    ./setup.sh -t all -h -c

COPY entrypoint.sh ~/entrypoint.sh
ENTRYPOINT [ "~/entrypoint.sh" ]
CMD [ "/bin/bash" ]