FROM rockylinux:9

# Install necessary packages
RUN dnf update -y && \
    dnf install -y git docker gcc g++ python3-devel && \
    dnf clean all

RUN /usr/bin/python3 -m pip install --upgrade apache-superset

WORKDIR /app

CMD ["bash"]
