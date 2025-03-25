# gitlab

[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.16-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)

Gitlab installation

**Platforms Supported**:

| Platform | Versions |
|----------|----------|
| Debian | 12 - Bookworm |

## ⚠️ Requirements

Ansible >= 2.16.

### Ansible role dependencies

None.

## ⚡ Installation

### ✏️ Example Playbook

<b>WARN - You must create the folder with certificates on your machine</b>

Basic usage is:

```yaml
- hosts: all
  roles:
    - role: gitlab
```

## ⚙️ Role Variables

Variables are divided in three types.

The **default vars** section shows you which variables you may
override in your ansible inventory. As a matter of fact, all variables should
be defined there for explicitness, ease of documentation as well as overall
role manageability.

The **context variables** are shown in section below hint you
on how runtime context may affects role execution.

### Default variables
Role default variables from `defaults/main.yml`.

| Variable Name | Value |
|---------------|-------|
| required_packages | - curl<br>- openssh-server<br>- ca-certificates<br>- perl<br> |
| gitlab_domain | localhost |
| gitlab_external_url | https://{{ gitlab_domain }}/ |
| gitlab_git_data_dir | /var/opt/gitlab/git-data |
| gitlab_edition | gitlab-ce |
| gitlab_version |  |
| gitlab_backup_path | /var/opt/gitlab/backups |
| gitlab_config_template | gitlab.rb.j2 |
| gitlab_redirect_http_to_https | False |
| gitlab_ssl_certificate | /etc/gitlab/ssl/{{ gitlab_domain }}.crt |
| gitlab_ssl_certificate_key | /etc/gitlab/ssl/{{ gitlab_domain }}.key |
| gitlab_create_self_signed_cert | True |
| gitlab_self_signed_cert_subj | /C=FR/ST=Occitanie/L=Toulouse/O=IT/CN={{ gitlab_domain }} |
| gitlab_ldap_enabled | False |
| gitlab_ldap_host | example.com |
| gitlab_ldap_port | 389 |
| gitlab_ldap_uid | sAMAccountName |
| gitlab_ldap_method | plain |
| gitlab_ldap_bind_dn | CN=Username,CN=Users,DC=example,DC=com |
| gitlab_ldap_password | password |
| gitlab_ldap_base | DC=example,DC=com |
| gitlab_smtp_enable | False |
| gitlab_smtp_address | smtp.server |
| gitlab_smtp_port | 465 |
| gitlab_smtp_user_name | smtp user |
| gitlab_smtp_password | smtp password |
| gitlab_smtp_domain | example.com |
| gitlab_smtp_authentication | login |
| gitlab_smtp_enable_starttls_auto | True |
| gitlab_smtp_tls | False |
| gitlab_smtp_openssl_verify_mode | none |
| gitlab_smtp_ca_path | /etc/ssl/certs |
| gitlab_smtp_ca_file | /etc/ssl/certs/ca-certificates.crt |
| gitlab_nginx_ssl_verify_client |  |
| gitlab_nginx_ssl_client_certificate |  |
| gitlab_restart_handler_failed_when | gitlab_restart.rc != 0 |
| gitlab_dependencies | - openssh-server<br>- postfix<br>- curl<br>- openssl<br>- tzdata<br> |
| gitlab_time_zone | UTC |
| gitlab_backup_keep_time | 604800 |
| gitlab_download_validate_certs | True |
| gitlab_default_theme | 2 |
| gitlab_email_enabled | False |
| gitlab_email_from | gitlab@example.com |
| gitlab_email_display_name | Gitlab |
| gitlab_email_reply_to | gitlab@example.com |
| gitlab_registry_enable | False |
| gitlab_registry_external_url | https://gitlab.example.com:4567 |
| gitlab_registry_nginx_ssl_certificate | /etc/gitlab/ssl/gitlab.crt |
| gitlab_registry_nginx_ssl_certificate_key | /etc/gitlab/ssl/gitlab.key |
| gitlab_letsencrypt_enable | False |
| gitlab_letsencrypt_contact_emails | - gitlab@example.com<br> |
| gitlab_letsencrypt_auto_renew_hour | 1 |
| gitlab_letsencrypt_auto_renew_minute | 30 |
| gitlab_letsencrypt_auto_renew_day_of_month | */7 |
| gitlab_letsencrypt_auto_renew | True |

### Context variables

Those variables from `vars/*.{yml,json}` are loaded dynamically during task
runtime using the `include_vars` module.

Variables loaded from `vars/main.yml`.

| Variable Name | Value |
|---------------|-------|
| gitlab_repository_installation_script_url | https://packages.gitlab.com/install/repositories/gitlab/{{ gitlab_edition }}/script.deb.sh |
