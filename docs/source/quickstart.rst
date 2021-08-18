Quickstart
==========

Installing
~~~~~~~~~~

Install `iepy` using ::

    pip install -U iepy

And than import using

.. code-block:: python3

    import iepy


Getting events
~~~~~~~~~~~~~~

To get events you can use

.. code-block:: python3

    iepy.getEvents(iepy.Date(12, 24))

to get the events on a date.
To get events on this day, use

.. code-block:: python3

    iepy.getTodayEvents()

Both of these functions return a list of lists of :class:`Event` one list contains the event from one year in every language.

Tweeting events
~~~~~~~~~~~~~~~

You can also tweet events, for this you will need the `tweepy <https://www.tweepy.org>`_ library

.. code-block:: python3

    for event in getTodayEvents():
        for eventLang in event:
            tweetEvent(
                eventLang,
                os.environ["consumerKey"],
                os.environ["consumerSecret"],
                os.environ["accessToken"],
                os.environ["accessTokenSecret"]
            )

If you don't supply ``accessToken`` and ``accessTokenSecret`` you will be promted with a verification link.