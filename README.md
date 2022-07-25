[![GitHub release](https://img.shields.io/github/v/release/colibris-xyz/iredapd-docker.svg?style=flat)](https://github.com/colibris-xyz/iredapd-docker/releases/latest)
[![GitHub license](https://img.shields.io/github/license/colibris-xyz/iredapd-docker)](https://github.com/colibris-xyz/iredapd-docker/blob/main/LICENSE)

# Docker image for iRedAPD

[iRedAPD](https://github.com/iredmail/iRedAPD) is a [Postfix policy server](http://www.postfix.org/SMTPD_POLICY_README.html) for the [iRedMail project](http://www.iredmail.org/). You will need a working iRedMail setup to be able to use this image.

## Basic usage

```console
$ docker run -d -p 127.0.0.1:7777:7777 --env-file .env ghcr.io/colibris-xyz/iredapd:latest
```

All the basic configuration is done by environment variables, see the list below.

## Environment variables configuration

- `PLUGINS` (default: `None`) - Comma separated list of plugins to activate

### Mail accounts backend configuration
- `DATABASE_BACKEND` (default: `ldap`) - The database backend to store mail accounts. Currently supported: `ldap`, `mysql`, `pgsql`.

__OpenLDAP backend__:
- `LDAP_URI` (not set by default) - LDAP server URI, prefix with `ldap://`.
- `LDAP_BASE_DN` (not set by default) - LDAP base DN. For example: `o=domains,dc=iredmail,dc=org`.
- `LDAP_BIND_DN` (not set by default) - LDAP bind DN user. For example: `cn=vmailadmin,dc=iredmail,dc=org`.
- `LDAP_BIND_PASSWORD` (not set by default) - LDAP bind DN password.
- `LDAP_ENABLE_TLS` (default: `False`) - use startTLS.

__SQL backends__:
- `VMAIL_DB_HOST` (not set by default) -  Hostname of the vmail database server.
- `VMAIL_DB_NAME` (default: `vmail`) - Name of the vmail database.
- `VMAIL_DB_USER` (default: `vmailadmin`) - Username for the vmail database.
- `VMAIL_DB_PASSWORD` (not set by default) - Password for the vmail database.
- `VMAIL_DB_PORT` (default: `3306`) - Port of the vmail database.

### iRedAPD database configuration (for greylisting, throttle)
- `IREDAPD_DB_HOST` (not set by default) -  Hostname of the iRedAPD database server.
- `IREDAPD_DB_NAME` (default: `iredapd`) - Name of the iRedAPD database.
- `IREDAPD_DB_USER` (default: `iredapd`) - Username for the iRedAPD database.
- `IREDAPD_DB_PASSWORD`  (not set by default) - Password for the iRedAPD database.
- `IREDAPD_DB_PORT` (default: `3306`) - Port of the iRedAPD database.

### Amavisd database configuration (for policy lookup and white/blacklists)

- `AMAVISD_DB_HOST` (not set by default) - Hostname of the amavisd-new database server.
- `AMAVISD_DB_NAME` (default: `amavisd`) - Name of the amavisd-new database.
- `AMAVISD_DB_USER` (default: `amavisd`) - Username for the amavisd-new database.
- `AMAVISD_DB_PASSWORD`  (not set by default) - Password for the amavisd-new database.
- `AMAVISD_DB_PORT` (default: `3306`) - Port of the amavisd-new database.

## Database initialization

Currently, there is no automatic database initialization / change management. If your database is not already initialized, you can retrieve the SQL files with the following command: `docker cp <iredadmin_container_id>:/app/SQL /tmp`, then use your favorite tool to initialize the database.
