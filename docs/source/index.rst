Reliable fast feedback for embedded systems
===========================================

with the goal to simplifiy Hardware in the loop testing during development, CI/CD and mass production


.. toctree::
   :maxdepth: 1
   :caption: Overview:

   Getting started <self>
   modules.rst

.. hint::

   To get started clone the repository with the following command:

   .. code-block:: shell

      git clone https://github.com/locomuco/loop-client.git

   We're using rye to manage our vitual environments, please follow the instalaltion instructions at https://rye-up.com/guide/installation/ to install rye.

   .. code-block:: shell

      curl -sSf https://rye-up.com/get | bash
      echo 'source "$HOME/.rye/env"' >> ~/.bashrc
      source ~/.bashrc
   
   Install dependencies with:

   .. code-block:: shell

      rye sync
