""" View HTML in browser. """


def view_html(html, rm=False):
    """
    View HTML in browser.

    `rm` : if True existing temporary files will be deleted
    """

    # So many imports :O
    import os
    import webbrowser
    import string
    import random

    # Remove preview random files
    if rm:
        for f in os.listdir('/tmp'):
            if f.startswith('py_view'):
                os.remove(os.path.join('/tmp', f))

    # Generate a new file
    rand = ''.join(random.choice(string.lowercase) for i in range(10))
    temp = '/tmp/py_view.%s.html' % rand
    with open(temp, 'w') as t:
        t.write(html)

    # View
    webbrowser.open('file://' + temp)
