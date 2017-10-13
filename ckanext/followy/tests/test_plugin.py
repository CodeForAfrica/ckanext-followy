"""Tests for plugin.py."""
import ckanext.followy.plugin as plugin
from mock import MagicMock
import unittest


class FollowyPluginTest(unittest.TestCase):

    def setUp(self):
        self._toolkit = plugin.toolkit
        plugin.toolkit = MagicMock()

    def tearDown(self):
        plugin.toolkit = self._toolkit

    def test_update_config(self):
        # Create instance
        self.plg_instance = plugin.FollowyPlugin()

        # Test
        config = MagicMock()
        self.plg_instance.update_config(config)
        plugin.toolkit.add_template_directory.assert_called_once_with(config, 'templates')

    def test_before_map(self):
        
        urls_set = 2

        # Create instance
        self.plg_instance = plugin.FollowyPlugin()

        # Test
        m = MagicMock()
        self.plg_instance.before_map(m)

        self.assertEquals(urls_set, m.connect.call_count)
        m.connect.assert_any_call(
            'user_dataset_followee', '/user/datasets/following/{id}',
            controller='ckanext.followy.controllers.ui_controller:DatasetFollowee',
            action='user_dataset_followee', conditions=dict(method=['GET']), ckan_icon='thumbs-up-alt')

        m.connect.assert_any_call(
            'dashboard_dataset_followee', '/dashboard/datasets/following',
            controller='ckanext.followy.controllers.ui_controller:DatasetFollowee',
            action='dashboard_dataset_followee', conditions=dict(method=['GET']), ckan_icon='thumbs-up-alt')
