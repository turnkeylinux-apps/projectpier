ProjectPier - Easy Online Collaboration
=======================================

`ProjectPier`_ is an application for managing tasks, projects and teams
through an intuitive web interface. Its focus is to enable project
management by facilitating group communication and help your
organization communicate, collaborate and get things done. It is similar
in functionality to commercial groupware/project management products.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- ProjectPier configurations:
   
   - Installed from upstream source code to /var/www/projectpier
   - Default to kampPro2 theme (similar to 37signals basecamp).
   - Configured to use dynamic root\_url (also via SSL).

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH, MySQL: username **root**


.. _ProjectPier: http://www.projectpier.org
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: http://www.adminer.org/
