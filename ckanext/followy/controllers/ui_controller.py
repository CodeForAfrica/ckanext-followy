import ckan.lib.base as base
import ckan.model as model
import ckan.plugins as plugins
import ckan.lib.helpers as helpers

from ckan.common import request

toolkit = plugins.toolkit
c = toolkit.c


class DatasetFollow(base.BaseController):

    def _get_context(self):
        return {'model': model, 'session': model.Session,
                'user': c.user, 'auth_user_obj': c.userobj}

    def following(self):


