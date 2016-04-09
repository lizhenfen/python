===============
compute service
===============

Compute v2

compute service delete
----------------------

Delete service command

.. program:: compute service delete
.. code:: bash

    os compute service delete
        <service>

.. _compute-service-delete:
.. describe:: <service>

    Compute service to delete (ID only)

compute service list
--------------------

List service command

.. program:: compute service list
.. code:: bash

    os compute service list
        [--host <host>]
        [--service <service>]
        [--long]

.. _compute-service-list:
.. describe:: --host <host>

    Name of host

.. describe:: --service <service>

    Name of service

.. describe:: --long

    List additional fields in output


compute service set
-------------------

Set service command

.. program:: compute service set
.. code:: bash

    os compute service set
        [--enable | --disable]
        [--disable-reason <reason>]
        <host> <service>

.. _compute-service-set:
.. option:: --enable

    Enable service (default)

.. option:: --disable

    Disable service

.. option:: --disable-reason <reason>

    Reason for disabling the service (in quotes)

.. describe:: <host>

    Name of host

.. describe:: <service>

    Name of service

