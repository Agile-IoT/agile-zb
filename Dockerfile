FROM resin/raspberrypi2-debian:jessie-20161010

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  python3-dbus \
  libdbus-1-dev \
  libdbus-glib-1-dev \
  python3-gi \
  python3-pip \
  build-essential \
  python3-dev \
  python3-tk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# resin-sync will always sync to /usr/src/app, so code needs to be here.
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY dbus_server dbus_server
COPY ge_link_bulb ge_link_bulb

