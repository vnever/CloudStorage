"""Generated client library for resourcesettings version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.resourcesettings.v1 import resourcesettings_v1_messages as messages


class ResourcesettingsV1(base_api.BaseApiClient):
  """Generated client library for service resourcesettings version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://resourcesettings.googleapis.com/'
  MTLS_BASE_URL = 'https://resourcesettings.mtls.googleapis.com/'

  _PACKAGE = 'resourcesettings'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ResourcesettingsV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new resourcesettings handle."""
    url = url or self.BASE_URL
    super(ResourcesettingsV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.folders_settings = self.FoldersSettingsService(self)
    self.folders = self.FoldersService(self)
    self.organizations_settings = self.OrganizationsSettingsService(self)
    self.organizations = self.OrganizationsService(self)
    self.projects_settings = self.ProjectsSettingsService(self)
    self.projects = self.ProjectsService(self)

  class FoldersSettingsService(base_api.BaseApiService):
    """Service class for the folders_settings resource."""

    _NAME = 'folders_settings'

    def __init__(self, client):
      super(ResourcesettingsV1.FoldersSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Returns a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist.

      Args:
        request: (ResourcesettingsFoldersSettingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1Setting) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/settings/{settingsId}',
        http_method='GET',
        method_id='resourcesettings.folders.settings.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ResourcesettingsFoldersSettingsGetRequest',
        response_type_name='GoogleCloudResourcesettingsV1Setting',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the settings that are available on the Cloud resource `parent`.

      Args:
        request: (ResourcesettingsFoldersSettingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1ListSettingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/settings',
        http_method='GET',
        method_id='resourcesettings.folders.settings.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken', 'view'],
        relative_path='v1/{+parent}/settings',
        request_field='',
        request_type_name='ResourcesettingsFoldersSettingsListRequest',
        response_type_name='GoogleCloudResourcesettingsV1ListSettingsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if the setting is flagged as read only. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only `name`, `local_value` and `etag`. The `metadata` and `effective_value` cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the `local_value` field.

      Args:
        request: (ResourcesettingsFoldersSettingsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1Setting) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/folders/{foldersId}/settings/{settingsId}',
        http_method='PATCH',
        method_id='resourcesettings.folders.settings.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='googleCloudResourcesettingsV1Setting',
        request_type_name='ResourcesettingsFoldersSettingsPatchRequest',
        response_type_name='GoogleCloudResourcesettingsV1Setting',
        supports_download=False,
    )

  class FoldersService(base_api.BaseApiService):
    """Service class for the folders resource."""

    _NAME = 'folders'

    def __init__(self, client):
      super(ResourcesettingsV1.FoldersService, self).__init__(client)
      self._upload_configs = {
          }

  class OrganizationsSettingsService(base_api.BaseApiService):
    """Service class for the organizations_settings resource."""

    _NAME = 'organizations_settings'

    def __init__(self, client):
      super(ResourcesettingsV1.OrganizationsSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Returns a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist.

      Args:
        request: (ResourcesettingsOrganizationsSettingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1Setting) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/settings/{settingsId}',
        http_method='GET',
        method_id='resourcesettings.organizations.settings.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ResourcesettingsOrganizationsSettingsGetRequest',
        response_type_name='GoogleCloudResourcesettingsV1Setting',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the settings that are available on the Cloud resource `parent`.

      Args:
        request: (ResourcesettingsOrganizationsSettingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1ListSettingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/settings',
        http_method='GET',
        method_id='resourcesettings.organizations.settings.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken', 'view'],
        relative_path='v1/{+parent}/settings',
        request_field='',
        request_type_name='ResourcesettingsOrganizationsSettingsListRequest',
        response_type_name='GoogleCloudResourcesettingsV1ListSettingsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if the setting is flagged as read only. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only `name`, `local_value` and `etag`. The `metadata` and `effective_value` cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the `local_value` field.

      Args:
        request: (ResourcesettingsOrganizationsSettingsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1Setting) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/organizations/{organizationsId}/settings/{settingsId}',
        http_method='PATCH',
        method_id='resourcesettings.organizations.settings.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='googleCloudResourcesettingsV1Setting',
        request_type_name='ResourcesettingsOrganizationsSettingsPatchRequest',
        response_type_name='GoogleCloudResourcesettingsV1Setting',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(ResourcesettingsV1.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsSettingsService(base_api.BaseApiService):
    """Service class for the projects_settings resource."""

    _NAME = 'projects_settings'

    def __init__(self, client):
      super(ResourcesettingsV1.ProjectsSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Returns a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist.

      Args:
        request: (ResourcesettingsProjectsSettingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1Setting) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/settings/{settingsId}',
        http_method='GET',
        method_id='resourcesettings.projects.settings.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ResourcesettingsProjectsSettingsGetRequest',
        response_type_name='GoogleCloudResourcesettingsV1Setting',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the settings that are available on the Cloud resource `parent`.

      Args:
        request: (ResourcesettingsProjectsSettingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1ListSettingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/settings',
        http_method='GET',
        method_id='resourcesettings.projects.settings.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken', 'view'],
        relative_path='v1/{+parent}/settings',
        request_field='',
        request_type_name='ResourcesettingsProjectsSettingsListRequest',
        response_type_name='GoogleCloudResourcesettingsV1ListSettingsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if the setting is flagged as read only. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only `name`, `local_value` and `etag`. The `metadata` and `effective_value` cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the `local_value` field.

      Args:
        request: (ResourcesettingsProjectsSettingsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1Setting) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/settings/{settingsId}',
        http_method='PATCH',
        method_id='resourcesettings.projects.settings.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='googleCloudResourcesettingsV1Setting',
        request_type_name='ResourcesettingsProjectsSettingsPatchRequest',
        response_type_name='GoogleCloudResourcesettingsV1Setting',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ResourcesettingsV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
