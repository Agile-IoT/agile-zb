FROM resin/armv7hf-debian:jessie-20161015

# Install dependencies
RUN apt-get clean && apt-get update && apt-get install -y \
  python3-dbus \
  libdbus-1-dev \
  libdbus-glib-1-dev \
  python3-gi \
  python3-pip \
  python3-dev \
  python3-tk \
  build-essential \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# resin-sync will always sync to /usr/src/app, so code needs to be here.
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY dbus_server dbus_server
COPY ge_link_bulb ge_link_bulb

