import ckan.lib.base as base
import ckan.model as model
import ckan.plugins as plugins
import ckan.authz as authz
import ckan.logic as logic
import ckan.lib.helpers as h

toolkit = plugins.toolkit
c = toolkit.c

abort = base.abort
NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized


class DatasetFollow(base.BaseController):

    def _get_context(self):
        return {'model': model, 'session': model.Session,
                'user': c.user, 'auth_user_obj': c.userobj}

    def user_dataset_followee(self):
        context = self._get_context()
        data_dict = {'id': c.userobj.id,
                     'user_obj': c.userobj,
                     'include_datasets': True,
                     'include_num_followers': True}

        followee_list = toolkit.get_action('dataset_followee_list')(context, data_dict)
        c.is_sysadmin = authz.is_sysadmin(c.user)

        try:
            user_dict = toolkit.get_action('user_show')(context, data_dict)
        except NotFound:
            abort(404, _('User not found'))
        except NotAuthorized:
            abort(403, _('Not authorized to see this page'))

        c.user_dict = user_dict
        c.is_myself = user_dict['name'] == c.user
        c.about_formatted = h.render_markdown(user_dict['about'])
        return toolkit.render('user/datasets_followee.html', extra_vars={'followees': followee_list})

    def dashboard_dataset_followee(self):
        context = self._get_context()
        data_dict = {'id': c.userobj.id,
                     'user_obj': c.userobj,
                     'include_datasets': True}

        followee_list = toolkit.get_action('dataset_followee_list')(context, data_dict)
        return toolkit.render('user/dashboard_datasets_followee.html', extra_vars={'followees': followee_list})


