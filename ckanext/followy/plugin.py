import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class FollowyPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'followy')

    # IRoutes

    def before_map(self, m):

        # List Datasets that a user is follow
        m.connect('user_dataset_follow', '/dashboard/datasets/follow',
                  controller='ckanext.followy.controllers.ui_controller:DatasetFollow',
                  action='following', conditions=dict(method=['GET']),
                  ckan_icon='thumbs-up-alt')

        return m

    def after_map(self, m):

        return m
