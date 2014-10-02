============================================
Using Font Awesome in PyGObject applications
============================================

:date: 2014-10-01T17:40-0600
:author: carlos-jenkins
:category: programming
:tags: python, gtk, font awesome
:slug: using-font-awesome-in-pygobject-applications

For those who doesn't know about `Font Awesome`_:

    "Font Awesome is a full suite of 479 pictographic icons for easy
    scalable vector graphics on websites".

    -- Font Awesome GitHub repository

"Websites"... well... you can use it in Gtk+ applications too :fa:`fa-smile-o`

In this example I'll use PyGObject, but any language that can use Gtk+ should
work. We will use the `Pango Markup Format`_ which is very similar to HTML.
With it, we can:

- Put Font Awesome icons in labels, buttons, etc.

  - Pretty much everywhere where Pango Markup is accepted.

- Change size of icons.
- Change color of icons.

We need to have the Font Awesome font installed in our systems, so go to
`Font Awesome`_ website and grab the lastest release. Unzip, and install
font ``fonts/FontAwesome.otf``.

Double click, install; or copy-paste it in ``.local/share/fonts``.

That's it, now we just need to use it using the codes from the `cheatsheet`_
like so:

.. code:: pycon

   >>> from gi.repository import Gtk
   >>> label = Gtk.Label()
   >>> markup = '<span fgcolor="#7c8dde" font_desc="FontAwesome 30">&#xf0e7;</span>'
   >>> label.set_markup(markup)

That's it. Here's how it looks like:

.. image:: /images/font_awesome_pygobject_animation.gif
   :alt: Font Awesome PyGObject animation

Here is a full example in a `Gist`_:

.. raw:: html

   <div class="gist">
      <script src="https://gist.github.com/carlos-jenkins/8eb6083c6db148743d74.js"></script>
   </div>


.. _Font Awesome: http://fontawesome.io/
.. _Pango Markup Format: https://developer.gnome.org/pango/stable/PangoMarkupFormat.html
.. _cheatsheet: http://fortawesome.github.io/Font-Awesome/cheatsheet/
.. _Gist: https://gist.github.com/carlos-jenkins/8eb6083c6db148743d74