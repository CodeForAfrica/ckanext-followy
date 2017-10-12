import ckan.plugins as plugins

toolkit = plugins.toolkit


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

        # Lists Datasets that a user is following on profile
        m.connect('user_dataset_followee', '/user/datasets/following/{id}',
                  controller='ckanext.followy.controllers.ui_controller:DatasetFollowee',
                  action='user_dataset_followee', conditions=dict(method=['GET']),
                  ckan_icon='thumbs-up-alt')

        # Lists Datasets that a user is following on dashboard
        m.connect('dashboard_dataset_followee', '/dashboard/datasets/following',
                  controller='ckanext.followy.controllers.ui_controller:DatasetFollowee',
                  action='dashboard_dataset_followee', conditions=dict(method=['GET']),
                  ckan_icon='thumbs-up-alt')

        return m

    def after_map(self, m):
        return m
