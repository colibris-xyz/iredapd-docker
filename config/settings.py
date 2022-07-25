import os
from distutils.util import strtobool

############################################################
# DO NOT MODIFY THIS LINE, IT'S USED TO IMPORT DEFAULT SETTINGS.
from libs.default_settings import *
############################################################

run_as_user = "nobody"
pid_file = "/tmp/iredapd.pid"

# Listen address and port.
listen_address = '0.0.0.0'
# Port for normal Postfix policy requests.
listen_port = 7777

# Log level: info, debug.
log_level = os.getenv('LOG_LEVEL', 'info')

# Enabled plugins.
plugins = os.getenv('PLUGINS').split(',') if os.getenv('PLUGINS') else []

# SRS
srs_secrets = []

# Database backend
backend = os.getenv('DATABASE_BACKEND', 'ldap').lower()

if backend == 'ldap':
    ldap_uri = os.getenv('LDAP_URI')
    ldap_basedn = os.getenv('LDAP_BASE_DN')
    ldap_binddn = os.getenv('LDAP_BIND_DN')
    ldap_bindpw = os.getenv('LDAP_BIND_PASSWORD')
    ldap_enable_tls = bool(strtobool(os.getenv('LDAP_ENABLE_TLS', 'False')))

elif backend == 'mysql' or backend == 'pgsql':
    vmail_db_server = os.getenv('VMAIL_DB_HOST')
    vmail_db_port = int(os.getenv('VMAIL_DB_PORT', '3306'))
    vmail_db_name = os.getenv('VMAIL_DB_NAME', 'vmail')
    vmail_db_user = os.getenv('VMAIL_DB_USER', 'vmailadmin')
    vmail_db_password = os.getenv('VMAIL_DB_PASSWORD')

# iRedAPD database, used for greylisting, throttle.
iredapd_db_server = os.getenv('IREDAPD_DB_HOST')
iredapd_db_port = os.getenv('IREDAPD_DB_PORT', '3306')
iredapd_db_name = os.getenv('IREDAPD_DB_NAME', 'iredapd')
iredapd_db_user = os.getenv('IREDAPD_DB_USER', 'iredapd')
iredapd_db_password = os.getenv('IREDAPD_DB_PASSWORD')

# For Amavisd policy lookup and white/blacklists.
amavisd_db_server = os.getenv('AMAVISD_DB_HOST')
amavisd_db_port = os.getenv('AMAVISD_DB_PORT', '3306')
amavisd_db_name = os.getenv('AMAVISD_DB_NAME', 'amavisd')
amavisd_db_user = os.getenv('AMAVISD_DB_USER', 'amavisd')
amavisd_db_password = os.getenv('AMAVISD_DB_PASSWORD')

# Trusted IP address or networks.
# Valid formats:
#   - Single IP address: 192.168.1.1
#   - Wildcard IP range: 192.168.1.*, 192.168.*.*, 192.168.*.1
#   - IP subnet: 192.168.1.0/24
MYNETWORKS = os.getenv('MYNETWORKS').split(',') if os.getenv('MYNETWORKS') else []

# Log smtp actions returned by plugins in SQL database (table `smtp_actions`).
LOG_SMTP_SESSIONS = bool(strtobool(os.getenv('LOG_SMTP_SESSIONS', 'False')))
