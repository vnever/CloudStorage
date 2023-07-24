# -*- coding: utf-8 -*- #
# Copyright 2023 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command to provision a new Spectrum Access System's deployment."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.spectrum_access import sas_portal_api
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.console import console_io


@base.Hidden
class Provision(base.DescribeCommand):
  """Provision a new Spectrum Access System's deployment.

  ## EXAMPLES

  The following command provisions a new SAS deployment:

    $ gcloud cbrs-spectrum-access provision --organization-name=MyOrgName
    --deployment-name=MyDeploymentName
  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        '--organization-name',
        required=False,
        help=(
            'The display name to use in case a new SAS Portal organization'
            ' needs to be created. If creating a deployment under an existing'
            ' organization then the organization-id flag must be set instead.'
        ),
    )
    parser.add_argument(
        '--deployment-name',
        required=False,
        help=(
            'The display name to use in case a new SAS Portal deployment needs'
            ' to be created. If not set, a default display name of the form'
            ' "[ID]" will be used where ID is the current Cloud Platform'
            ' Project ID.'
        ),
    )
    parser.add_argument(
        '--organization-id',
        required=False,
        type=int,
        help=(
            'The id of the organization to create a new deployment under.'
            ' If left empty a new organization will be created with the name'
            ' entered via the organization-name flag. Either this or'
            ' organization-name must be set.'
        ),
    )

  def Run(self, args):
    if not args.organization_name and not args.organization_id:
      raise exceptions.OneOfArgumentsRequiredException(
          ['organization-name', 'organization-id'],
          'Either organization-name or organization-id must be set. Use'
          ' organization-name when creating a new organization and'
          ' organization-id when create a deployment under an existing'
          ' organization.',
      )

    if args.organization_name and args.organization_id:
      raise exceptions.InvalidArgumentException(
          'organization-name, organization-id',
          'Either organization-name or organization-id must be set but not'
          ' both. Use organization-name when creating a new organization and'
          ' organization-id when create a deployment under an existing'
          ' organization.',
      )

    log.status.Print(
        'This command will enable the Spectrum Access System'
        ' and create a new SAS deployment for your'
        ' organization. The Spectrum Access System is governed by your Google'
        ' Cloud Agreement or Cloud Master Agreement and the Spectrum Access'
        ' System specific terms at cloud.google.com/terms.'
    )
    console_io.PromptContinue(
        default=False,
        cancel_on_no=True,
        prompt_string='Do you accept the agreement?',
    )

    base.EnableUserProjectQuota()
    client = sas_portal_api.GetClientInstance().customers
    message_module = sas_portal_api.GetMessagesModule()
    req = message_module.SasPortalProvisionDeploymentRequest()
    req.newOrganizationDisplayName = args.organization_name
    req.newDeploymentDisplayName = args.deployment_name
    req.organizationId = args.organization_id

    result = client.ProvisionDeployment(req)
    if not result.errorMessage:
      portal_api_override = properties.VALUES.api_endpoint_overrides.Property(
          'sasportal'
      ).Get()
      sas_portal_url = 'g.co/sasportal'
      if portal_api_override and ('prod-tt-sasportal' in portal_api_override):
        sas_portal_url = 'https://wirelessconnectivity.google.com/test-sas'

      project = properties.VALUES.core.project.Get()

      log.status.Print(
          'A new SAS deployment with userID: {}  has been created. Go to'
          ' {} to check spectrum availability, pre-register CBSDs,'
          ' check CBSD status and manage users.'.format(project, sas_portal_url)
      )

    return result
