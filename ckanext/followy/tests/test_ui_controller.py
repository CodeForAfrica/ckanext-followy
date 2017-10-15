import ckanext.followy.controllers.ui_controller as controller
import unittest

from mock import MagicMock


class UIControllerTest(unittest.TestCase):

    def setUp(self):

        self._toolkit = controller.toolkit
        controller.toolkit = MagicMock()

        self._c = controller.c
        controller.c = MagicMock()

        self._model = controller.model
        controller.model = MagicMock()

        self.expected_context = {
            'model': controller.model,
            'session': controller.model.Session,
            'user': controller.c.user,
            'auth_user_obj': controller.c.userobj
        }

        self.controller_instance = controller.DatasetFollowee()

    def tearDown(self):
        controller.toolkit = self._toolkit
        controller.c = self._c
        controller.model = self._model

    def test_dataset_followee(self):

        action_name = 'dataset_followee_list'

        data_dict = {'id': controller.c.userobj.id,
                     'user_obj': controller.c.userobj,
                     'include_datasets': True}

        followee_list = controller.toolkit.get_action(action_name)(self.expected_context, data_dict)

        # Create Instance
        self.ctl_instance = controller.DatasetFollowee()

        # Test
        self.ctl_instance.dashboard_dataset_followee()
        controller.toolkit.get_action(action_name).assert_called_with(self.expected_context, data_dict)
        controller.toolkit.render.assert_called_once_with('user/dashboard_datasets_followee.html',
                                                          extra_vars={'followees': followee_list[::-1]})
