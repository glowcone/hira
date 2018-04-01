"""Generated client library for replicapoolupdater version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.replicapoolupdater.v1beta1 import replicapoolupdater_v1beta1_messages as messages


class ReplicapoolupdaterV1beta1(base_api.BaseApiClient):
  """Generated client library for service replicapoolupdater version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://www.googleapis.com/replicapoolupdater/v1beta1/'

  _PACKAGE = u'replicapoolupdater'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only', u'https://www.googleapis.com/auth/replicapool', u'https://www.googleapis.com/auth/replicapool.readonly']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ReplicapoolupdaterV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new replicapoolupdater handle."""
    url = url or self.BASE_URL
    super(ReplicapoolupdaterV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.rollingUpdates = self.RollingUpdatesService(self)
    self.rollout = self.RolloutService(self)
    self.zoneOperations = self.ZoneOperationsService(self)

  class RollingUpdatesService(base_api.BaseApiService):
    """Service class for the rollingUpdates resource."""

    _NAME = u'rollingUpdates'

    def __init__(self, client):
      super(ReplicapoolupdaterV1beta1.RollingUpdatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Cancels an update. The update must be PAUSED before it can be cancelled. This has no effect if the update is already CANCELLED.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollingUpdates.cancel',
        ordered_params=[u'project', u'zone', u'rollingUpdate'],
        path_params=[u'project', u'rollingUpdate', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/cancel',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesCancelRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Returns information about an update.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RollingUpdate) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'replicapoolupdater.rollingUpdates.get',
        ordered_params=[u'project', u'zone', u'rollingUpdate'],
        path_params=[u'project', u'rollingUpdate', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates/{rollingUpdate}',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesGetRequest',
        response_type_name=u'RollingUpdate',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      """Inserts and starts a new update.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollingUpdates.insert',
        ordered_params=[u'project', u'zone'],
        path_params=[u'project', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates',
        request_field=u'rollingUpdate',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesInsertRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists recent updates for a given managed instance group, in reverse chronological order and paginated format.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RollingUpdateList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'replicapoolupdater.rollingUpdates.list',
        ordered_params=[u'project', u'zone'],
        path_params=[u'project', u'zone'],
        query_params=[u'filter', u'maxResults', u'pageToken'],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesListRequest',
        response_type_name=u'RollingUpdateList',
        supports_download=False,
    )

    def ListInstanceUpdates(self, request, global_params=None):
      """Lists the current status for each instance within a given update.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesListInstanceUpdatesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (InstanceUpdateList) The response message.
      """
      config = self.GetMethodConfig('ListInstanceUpdates')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListInstanceUpdates.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'replicapoolupdater.rollingUpdates.listInstanceUpdates',
        ordered_params=[u'project', u'zone', u'rollingUpdate'],
        path_params=[u'project', u'rollingUpdate', u'zone'],
        query_params=[u'filter', u'maxResults', u'pageToken'],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/instanceUpdates',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesListInstanceUpdatesRequest',
        response_type_name=u'InstanceUpdateList',
        supports_download=False,
    )

    def Pause(self, request, global_params=None):
      """Pauses the update in state from ROLLING_FORWARD or ROLLING_BACK. Has no effect if invoked when the state of the update is PAUSED.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesPauseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Pause')
      return self._RunMethod(
          config, request, global_params=global_params)

    Pause.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollingUpdates.pause',
        ordered_params=[u'project', u'zone', u'rollingUpdate'],
        path_params=[u'project', u'rollingUpdate', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/pause',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesPauseRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Resume(self, request, global_params=None):
      """Continues an update in PAUSED state. Has no effect if invoked when the state of the update is ROLLED_OUT.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesResumeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Resume')
      return self._RunMethod(
          config, request, global_params=global_params)

    Resume.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollingUpdates.resume',
        ordered_params=[u'project', u'zone', u'rollingUpdate'],
        path_params=[u'project', u'rollingUpdate', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/resume',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesResumeRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Rollback(self, request, global_params=None):
      """Rolls back the update in state from ROLLING_FORWARD or PAUSED. Has no effect if invoked when the state of the update is ROLLED_BACK.

      Args:
        request: (ReplicapoolupdaterRollingUpdatesRollbackRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Rollback')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rollback.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollingUpdates.rollback',
        ordered_params=[u'project', u'zone', u'rollingUpdate'],
        path_params=[u'project', u'rollingUpdate', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/rollback',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRollingUpdatesRollbackRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class RolloutService(base_api.BaseApiService):
    """Service class for the rollout resource."""

    _NAME = u'rollout'

    def __init__(self, client):
      super(ReplicapoolupdaterV1beta1.RolloutService, self).__init__(client)
      self._upload_configs = {
          }

    def Abandon(self, request, global_params=None):
      """Abandon a rollout, leaving the IGM in the state it is already configured. This allows you to apply a new rollout to the IGM.

      Args:
        request: (ReplicapoolupdaterRolloutAbandonRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Abandon')
      return self._RunMethod(
          config, request, global_params=global_params)

    Abandon.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollout.abandon',
        ordered_params=[u'project', u'zone', u'rollout'],
        path_params=[u'project', u'rollout', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollouts/{rollout}/abandon',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRolloutAbandonRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

    def Commit(self, request, global_params=None):
      """Commits a rollout, so that it is final and can not be rolled back.

      Args:
        request: (ReplicapoolupdaterRolloutCommitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Commit')
      return self._RunMethod(
          config, request, global_params=global_params)

    Commit.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollout.commit',
        ordered_params=[u'project', u'zone', u'rollout'],
        path_params=[u'project', u'rollout', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollouts/{rollout}/commit',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRolloutCommitRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Get the details of a rollout.

      Args:
        request: (ReplicapoolupdaterRolloutGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'replicapoolupdater.rollout.get',
        ordered_params=[u'project', u'zone', u'rollout'],
        path_params=[u'project', u'rollout', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollouts/{rollout}',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRolloutGetRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      """Inserts and starts a new rollout.

      Args:
        request: (ReplicapoolupdaterRolloutInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollout.insert',
        ordered_params=[u'project', u'zone'],
        path_params=[u'project', u'zone'],
        query_params=[u'updatePolicyInitialisationMethod'],
        relative_path=u'projects/{project}/zones/{zone}/rollouts',
        request_field=u'rollout',
        request_type_name=u'ReplicapoolupdaterRolloutInsertRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Resume a rollout. This lets the rollout continue updating instances after a pause.

      Args:
        request: (ReplicapoolupdaterRolloutListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRolloutResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'replicapoolupdater.rollout.list',
        ordered_params=[u'project', u'zone'],
        path_params=[u'project', u'zone'],
        query_params=[u'filter', u'maxResults', u'pageToken'],
        relative_path=u'projects/{project}/zones/{zone}/rollouts',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRolloutListRequest',
        response_type_name=u'ListRolloutResponse',
        supports_download=False,
    )

    def Pause(self, request, global_params=None):
      """Pause the application of a rollout. This stops the update, and the instances managed by the instance group manager do not change their instance templates.

      Args:
        request: (ReplicapoolupdaterRolloutPauseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Pause')
      return self._RunMethod(
          config, request, global_params=global_params)

    Pause.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollout.pause',
        ordered_params=[u'project', u'zone', u'rollout'],
        path_params=[u'project', u'rollout', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollouts/{rollout}/pause',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRolloutPauseRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

    def Rampup(self, request, global_params=None):
      """Change the amount of instances within an IGM that should be updated to the new instance template.

      Args:
        request: (ReplicapoolupdaterRolloutRampupRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Rampup')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rampup.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollout.rampup',
        ordered_params=[u'project', u'zone', u'rollout'],
        path_params=[u'project', u'rollout', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollouts/{rollout}/rampup',
        request_field=u'rampUpRolloutRequest',
        request_type_name=u'ReplicapoolupdaterRolloutRampupRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

    def Resume(self, request, global_params=None):
      """Resume a rollout. This lets the rollout continue updating instances after a pause.

      Args:
        request: (ReplicapoolupdaterRolloutResumeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Resume')
      return self._RunMethod(
          config, request, global_params=global_params)

    Resume.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollout.resume',
        ordered_params=[u'project', u'zone', u'rollout'],
        path_params=[u'project', u'rollout', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollouts/{rollout}/resume',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRolloutResumeRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

    def Rollback(self, request, global_params=None):
      """Rollback a rollout, cancelling the update and changing all instances with the updated version to have the instanceTemplateToRollback template.

      Args:
        request: (ReplicapoolupdaterRolloutRollbackRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Rollout) The response message.
      """
      config = self.GetMethodConfig('Rollback')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rollback.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'replicapoolupdater.rollout.rollback',
        ordered_params=[u'project', u'zone', u'rollout'],
        path_params=[u'project', u'rollout', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/rollouts/{rollout}/rollback',
        request_field='',
        request_type_name=u'ReplicapoolupdaterRolloutRollbackRequest',
        response_type_name=u'Rollout',
        supports_download=False,
    )

  class ZoneOperationsService(base_api.BaseApiService):
    """Service class for the zoneOperations resource."""

    _NAME = u'zoneOperations'

    def __init__(self, client):
      super(ReplicapoolupdaterV1beta1.ZoneOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Retrieves the specified zone-specific operation resource.

      Args:
        request: (ReplicapoolupdaterZoneOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'replicapoolupdater.zoneOperations.get',
        ordered_params=[u'project', u'zone', u'operation'],
        path_params=[u'operation', u'project', u'zone'],
        query_params=[],
        relative_path=u'projects/{project}/zones/{zone}/operations/{operation}',
        request_field='',
        request_type_name=u'ReplicapoolupdaterZoneOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Retrieves the list of Operation resources contained within the specified zone.

      Args:
        request: (ReplicapoolupdaterZoneOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OperationList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'replicapoolupdater.zoneOperations.list',
        ordered_params=[u'project', u'zone'],
        path_params=[u'project', u'zone'],
        query_params=[u'filter', u'maxResults', u'pageToken'],
        relative_path=u'projects/{project}/zones/{zone}/operations',
        request_field='',
        request_type_name=u'ReplicapoolupdaterZoneOperationsListRequest',
        response_type_name=u'OperationList',
        supports_download=False,
    )
