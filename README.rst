chimera-optec plugin
====================

A chimera_ plugin for OPTEC_ bus devices.

Usage
-----

Install chimera_ on your computer, and then, this package. Edit the configuration file adding one of the
supported OPTEC focusers as on the example below.

Installation
------------

Besides chimera_, ``chimera-optec`` depends only of pyserial_.

::

    pip install -U git+https://github.com/astroufsc/chimera-optec.git


Configuration Examples
----------------------

Here goes examples of the configuration to be added on ``chimera.config`` file.

* `Optec TCF-S`_ focuser

::

    focuser:
      type: OptecTCFS
      name: optec
      device: COM6          # /dev/ttyS?? on linux

Tested Hardware
---------------

This plugin was tested on these hardware:

* `Optec TCF-S`_ focuser


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-optec/

.. _chimera: https://www.github.com/astroufsc/chimera/
.. _pyserial: http://pyserial.sourceforge.net/
.. _JMI Smart 232: http://www.jimsmobile.com/
.. _LNA: http://www.lna.br/
.. _MEADE LX200: http://www.meade.com/products/telescopes/lx200.html
.. _Optec TCF-S: http://www.optecinc.com/astronomy/catalog/tcf/tcf-s.htm
.. _OPTEC: http://www.optecinc.com/
