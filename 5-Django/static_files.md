To Initialize Your Project And Make It Ready To Start, You Need To Find This Line Of Code :

`STATIC_URL = 'static/'`

Add This Code After That Line :

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

The Final Output Must Be Something Like :

```
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

After That You Can Make A Directory Named "`static`" And Put Any Static File You Want In There.
