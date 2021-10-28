FROM python:3.7.12-slim

LABEL maintainer="mariusz.rokita@gmail.com"

# No interaction is needed while installing or upgrading the system via apt.
ARG DEBIAN_FRONTEND=noninteractive

# Tools and prerequisites needed down the road
RUN apt-get update && apt-get -y install --no-install-recommends gcc g++ curl gnupg2 procps \
# Prerequisites for Python ODBC library and installs necessary locales
        unixodbc unixodbc-dev apt-transport-https locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen \
# Install ODBC support for MS SQL Server
# (more info: https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017)
    && curl --silent https://packages.microsoft.com/keys/microsoft.asc | apt-key add -; \
       curl --silent https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list; \
       apt-get update \
    && ACCEPT_EULA=Y apt-get -y install --no-install-recommends msodbcsql17 \
# Cleanup files to reduce image size
    && apt-get autoremove -y \
    &&  apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Do one simple thing - print out python version
CMD ["python", "--version"]