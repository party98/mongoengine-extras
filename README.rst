====================
mongoengine-extras
====================

mongoengine-extras is a collection of fields (and possibly other features
later) not included in MongoEngine, and which do not necessarily need to
be included in MongoEngine.

Currently the only features are two fields, a SlugField (as found in Django)
and an AutoSlugField. The latter is designed to enforce a unique, auto-
incremented slug value. It should be used in the same way as the 
AutoSlugField in django-extensions, although it's not quite there yet. For
now you simply provide the field with the source string and the field will
store a unique, auto-incremented slug.

Installing
===========

Use pip::

    pip install mongoengine-extras

Or download the source::

    python setup.py install

Dependencies
============

mongoengine-extras requires MongoEngine (which requires pymongo).

Tests
=====

The tests can by run with `python setup.py test`. Tests require a MongoDB 
database running on the standard port.

Authors
=======

* Ben Lopatin (`bennylope <https://github.com/bennylope>`_)
* Esteban Feldman (`eka <https://github.com/eka>`_)

License
=======

Public domain
