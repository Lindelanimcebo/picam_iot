=========
picam_iot
=========


.. image:: https://img.shields.io/pypi/v/picam_iot.svg
        :target: https://pypi.python.org/pypi/picam_iot

.. image:: https://img.shields.io/travis/lindelanimcebo/picam_iot.svg
        :target: https://travis-ci.com/lindelanimcebo/picam_iot

.. image:: https://readthedocs.org/projects/picam-iot/badge/?version=latest
        :target: https://picam-iot.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/lindelanimcebo/picam_iot/shield.svg
     :target: https://pyup.io/repos/github/lindelanimcebo/picam_iot/
     :alt: Updates



picam_iot provides simple interfacing with the picam V2 and intergrates it with Python computer vision or image processing libraries.


* Free software: MIT license
* Documentation: https://picam-iot.readthedocs.io.


Features
--------

* Basic image and video capture and recording
* Face detection captured or existing images
* Motion detection from videos
* Local storage management for images and videos
* Dropbox storage management for images and videos

Usage
-------

Requirements
^^^^^^^^^^^^^

* `Raspberry pi camera library`_
* OpenCV_
* `Dropbox Core API account and access token`_
*  Enough storage on the raspberry pi, 3GB recommended minimum

Get Started
^^^^^^^^^^^^^

install dependencies:

        $ pip3 install -requirements_dev.txt

basic usage:

        >>> from picam_iot import *
        >>> img = image() # image management class
        >>> vid = video() # video management class
        >>> dpx = dropbox_storage(access_token = "<access_token from dropbox>")


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Raspberry pi camera library`: https://picamera.readthedocs.io/en/release-1.13/
.. _OpenCV : https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/
.. _`Dropbox Core API account and access token` : https://www.dropbox.com/developers