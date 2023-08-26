By Default Django Rest Framework Returns a Page That Made By Themselves. Most Of
The Times Its Not What We Need And We Want To Return Response As Json Not A Page.
For This Purpose We Need To Use Json Renderer On Django Rest Framework.

You Have To Set You Default Renderer In "`settings.py`" in "`settings`" Directory.

It Should Be Something Like That :

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    # Other Settings ...
}
``````
