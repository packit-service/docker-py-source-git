#!/bin/bash
set -ex
# helpful commands to diagnose current env
id
rpm -q docker
systemctl status docker
ls -lha /var/run/docker.sock
exec pytest-3 -v /usr/libexec/installed-tests/python-docker/tests/integration/
