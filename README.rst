RobotFramework Requests Checker Library
=======================================

|Build Status|

Short Description
-----------------

`Robot Framework`_ library for checking HTTP response status code, based on `Requests`_ library.

Installation
------------

::

    pip install robotframework-requestschecker

Documentation
-------------

See keyword documentation for robotframework-requestschecker library in
folder ``docs``.

Example
-------
+---------------+---------------------------------------+-----------------------------+------------------------+----------+
|  Test cases   |                 Action                |           Argument          |        Argument        | Argument |
+===============+=======================================+=============================+========================+==========+
|  Simple Test  | RequestsLibrary.Create session        | Alias                       | http://www.example.com |          |
+---------------+---------------------------------------+-----------------------------+------------------------+----------+
|               | ${response}=                          | RequestsLibrary.Get request | Alias                  | /        |
+---------------+---------------------------------------+-----------------------------+------------------------+----------+
|               | RequestsChecker.Check Response Status | ${response}                 | 204                    |          |
+---------------+---------------------------------------+-----------------------------+------------------------+----------+


License
-------

Apache License 2.0

.. _Robot Framework: http://www.robotframework.org
.. _Requests: http://docs.python-requests.org/en/latest

.. |Build Status| image:: https://travis-ci.org/peterservice-rnd/robotframework-requestschecker.svg?branch=master
   :target: https://travis-ci.org/peterservice-rnd/robotframework-requestschecker