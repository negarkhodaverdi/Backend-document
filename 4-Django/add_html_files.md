To Add Your Templates ( Html Files ) You Have To Create A Directory Named "`templates`"
after That You Want To Add Your HTML Files There.

Then You Need To Add "`templates`" Directory As A Template Directory To Your Django
App. For This You Have To Go To "`settings.py`" on "`settings`" Folder.After That
Find The "`TEMPLATES`" Variable There.
It Should Be Something Like This :

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

After You Find That You Have To Add Your Folder Name ("`templates`") To '`DIRS`' In
This Dictionary. It Means After You Set It, It Should Be :

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Now You Can Add Any HTML File You Want !
