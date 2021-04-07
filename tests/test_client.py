import unittest

from unittest import TestCase
from energy_feed.client import EnergyFeedClient
from energy_feed.news_feed import NewsFeed


class TestEnergyFeedClient(TestCase):

    """Will perform a unit test for the `EnergyFeedClient` object."""

    def setUp(self) -> None:
        """Set up the `EnergyFeedClient` object."""

        self.client = EnergyFeedClient()

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `EnergyFeedClient` object"""

        self.assertIsInstance(self.client, EnergyFeedClient)

    def test_creates_instance_of_news_feed(self):
        """Create an instance and make sure it's a `NewsFeed` object"""

        self.assertIsInstance(self.client.news_feed(), NewsFeed)

    def tearDown(self) -> None:
        """Teardown the `EnergyFeedClient` object."""

        del self.client


if __name__ == '__main__':
    unittest.main()
