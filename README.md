[![Ansible Collection](https://img.shields.io/badge/dynamic/json?color=orange&style=flat&label=collection&prefix=v&url=https://galaxy.ansible.com/api/v3/collections/tonyskapunk/httpbin/&query=highest_version.version)](https://galaxy.ansible.com/ui/repo/published/tonyskapunk/httpbin/)
[![GitHub tag](https://img.shields.io/github/tag/tonyskapunk/ansible-collection-httpbin.svg)](https://github.com/tonyskapunk/ansible-collection-httpbin/tags)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/tonyskapunk/ansible-collection-httpbin)](https://github.com/tonyskapunk/ansible-collection-httpbin/tags)
[![GitHub Contributors](https://img.shields.io/github/contributors/tonyskapunk/ansible-collection-httpbin)](https://github.com/tonyskapunk/ansible-collection-httpbin/tags)
[![Ansible Galaxy](https://github.com/tonyskapunk/ansible-collection-httpbin/actions/workflows/publish.yml/badge.svg)](https://github.com/tonyskapunk/ansible-collection-httpbin/actions/workflows/publish.yml)
[![Module Testing](https://github.com/tonyskapunk/ansible-collection-httpbin/actions/workflows/module-testing.yml/badge.svg)](https://github.com/tonyskapunk/ansible-collection-httpbin/actions/workflows/module-testing.yml)
[![Role testing](https://github.com/tonyskapunk/ansible-collection-httpbin/actions/workflows/role-testing.yml/badge.svg)](https://github.com/tonyskapunk/ansible-collection-httpbin/actions/workflows/role-testing.yml)


# Ansible Collection - tonyskapunk.httpbin

A collection of modules to interact with httpbin.org service or an httpbin self-hosted instance.

> [!IMPORTANT]
> This collection is for educational purposes.
> This collection is not recommended for production environments, [ansible.builtin.get_url](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/get_url_module.html) is a better option

## Ansible version compatibility

The collection is tested and supported with: `ansible >= 2.16`

## Installing the collection

```shell
ansible-galaxy collection install tonyskapunk.httpbin
```

You can also include it in a `requirements.yml` file and install it via ansible-galaxy collection install -r `requirements.yml`, using the format:

```yaml
---
collections:
  - name: tonyskapunk.httpbin
```

## Using this collection

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `tonyskapunk.httpbin.http_methods`:

```yaml
- name: Using httpbin
  hosts: localhost
  tasks:
    - name: GET
      tonyskapunk.httpbin.http_methods:
```

or you can add full namespace and collection name in the `collections` element in your playbook

```yaml
- name: Using httpbin
  hosts: localhost
  collection:
    - tonyskapunk.httpbin
  tasks:
    - name: GET
     httpbin:
```

## License

GPL-3.0-or-later