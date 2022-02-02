# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.apps import AppConfig
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ForumConfig(AppConfig):
    """
    A class for configuring the forum app
    """
    name = "forum"

    def ready(self):
        """
        Imports signals
        Args:
            self (object): self.
        Returns:
            n/a
        """
        import forum.signals
