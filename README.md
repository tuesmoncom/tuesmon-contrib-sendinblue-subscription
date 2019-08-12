**NOTE: *This plugin is deprecated since Dec'16***

Tuesmon Contrib Sendinblue Subscription
=====================================

![Kaleidos Project](http://kaleidos.net/static/img/badge.png "Kaleidos Project")
[![Managed with Tuesmon.com](https://manage.tuesmon.com/support/images/tuesmon-badge-gh.png)](https://tuesmon.com "Managed with Tuesmon.com")

Plugin to subscribe and unsubscribe users to the newsletter and user list in Sendinblue


Installation
------------

### Configure Sendinblue

In Sendinblue you have to add two custom attributes to your contacts.

1 - Open Sendinblue.
2 - Go to `Settings` > `Attributes & CRM`
3 - Add the attributes:
    - Remove 'SURNAME' and 'NAME'
    - Add 'FULL_NAME' and 'USERNAME' (text type both of them).


### Production env

#### Tuesmon Back

In your Tuesmon back python virtualenv install the pip package `tuesmon-contrib-sendinblue-subscription` with:

```bash
  pip install -e "git+https://github.com/tuesmoncom/tuesmon-contrib-sendinblue-subscription.git@stable#egg=tuesmon-contrib-sendinblue-subscription&subdirectory=back"
```

Then modify in `tuesmon-back` your `settings/local.py` and include this line:

```python
  SENDINBLUE_NEWSLETTER_LIST_ID = "my-newsletter-list-id"
  SENDINBLUE_TUESMON_USERS_LIST_ID = "my-tuesmon-user-list-id"
  SENDINBLUE_API_KEY = "XXXXXXXXXXXXXXXXX"

  INSTALLED_APPS += ["tuesmon_contrib_sendinblue_subscription"]
```


#### Tuesmon Front

Download in your `dist/plugins/` directory of Tuesmon front the `tuesmon-contrib-sendinblue-subscription` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/tuesmoncom/tuesmon-contrib-sendinblue-subscription/branches/stable/front/dist" "sendinblue-subscription"
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/sendinblue-subscription/sendinblue-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/sendinblue-subscription/sendinblue-subscription.json"
    ]
...
```


### Dev env

#### Tuesmon Back

Clone the repo and

```bash
  cd tuesmon-contrib-sendinblue-subscription/back
  workon tuesmon
  pip install -e .
```

Then modify in `tuesmon-back` your `settings/local.py` and include this line:

```python
  MAILCHIMP_NEWSLETTER_ID = "my-newsletter"
  MAILCHIMP_API_KEY = "XXXXXXXXXXXXXXXXX"

  INSTALLED_APPS += ["tuesmon_contrib_sendinblue_subscription"]
```


#### Tuesmon Front

After clone the repo link `dist` in `tuesmon-front` plugins directory:

```bash
  cd tuesmon-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../tuesmon-contrib-sendinblue-subscription/front/dist sendinblue-subscription
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/sendinblue-subscription/sendinblue-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/sendinblue-subscription/sendinblue-subscription.json"
    ]
...
```

In the plugin source dir `tuesmon-contrib-sendinblue-subscription` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.
