# -*- coding: utf-8 -*- #
# Copyright 2023 Google Inc. All Rights Reserved.
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
"""`gcloud dataplex datascans update` command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dataplex import datascan
from googlecloudsdk.api_lib.dataplex import util as dataplex_util
from googlecloudsdk.api_lib.util import exceptions as gcloud_exception
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.dataplex import resource_args
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.core import log


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class DataQuality(base.Command):
  """Update a Dataplex data quality scan job."""

  detailed_help = {
      'EXAMPLES': """\

            Update a Dataplex data quality scan job.

            Represents a user-visible job which provides the insights for the
            related data source and generates queries based on the rules and runs against
            the data to get data quality check results.

            E.g., command to update description of a data quality scan `data-quality-datascan`
            in project `test-project` located in `us-central1`:
            dataplex datascans update data-quality data-quality-datascan --project=test-project --location=us-central1 --description="Description is updated."

          """,
  }

  @staticmethod
  def Args(parser):
    resource_args.AddDatascanResourceArg(
        parser, 'to update a data quality scan for.'
    )
    parser.add_argument(
        '--description',
        required=False,
        help='Description of the data quality scan',
    )
    parser.add_argument(
        '--display-name',
        required=False,
        help='Display name of the data quality scan',
    )
    parser.add_argument(
        '--data-quality-spec-file',
        help=(
            'path to the JSON/YAML file containing the spec for'
            ' the data quality scan. The json representation reference:'
            ' https://cloud.google.com/dataplex/docs/reference/rest/v1/DataQualitySpec'
        ),
    )
    execution_spec = parser.add_group(
        help='Data quality scan execution settings.'
    )
    trigger = execution_spec.add_group(
        mutex=True, help='Data quality scan scheduling and trigger settings'
    )
    trigger.add_argument(
        '--on-demand',
        type=bool,
        help=(
            'If set, the scan runs one-time shortly after data quality scan'
            ' updation.'
        ),
    )
    trigger.add_argument(
        '--schedule',
        help=(
            'Cron schedule (https://en.wikipedia.org/wiki/Cron) for running'
            ' scans periodically. To explicitly set a timezone to the cron tab,'
            ' apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or'
            ' "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid'
            ' string from IANA time zone database. For example,'
            ' `CRON_TZ=America/New_York 1 * * * *` or `TZ=America/New_York 1 *'
            ' * * *`. This field is required for RECURRING scans.'
        ),
    )
    async_group = parser.add_group(
        mutex=True,
        required=False,
        help='At most one of --async | --validate-only can be specified.',
    )
    async_group.add_argument(
        '--validate-only',
        action='store_true',
        default=False,
        help="Validate the update action, but don't actually perform it.",
    )
    base.ASYNC_FLAG.AddToParser(async_group)
    labels_util.AddCreateLabelsFlags(parser)

  @gcloud_exception.CatchHTTPErrorRaiseHTTPException(
      'Status code: {status_code}. {status_message}.'
  )
  def Run(self, args):
    update_mask = datascan.GenerateUpdateMask(args)
    if len(update_mask) < 1:
      raise exceptions.HttpException(
          'Update commands must specify at least one additional parameter to'
          ' change.'
      )
    datascan_ref = args.CONCEPTS.datascan.Parse()
    dataplex_client = dataplex_util.GetClientInstance()
    message = dataplex_util.GetMessageModule()
    setattr(args, 'scan_type', 'QUALITY')
    update_req_op = dataplex_client.projects_locations_dataScans.Patch(
        message.DataplexProjectsLocationsDataScansPatchRequest(
            name=datascan_ref.RelativeName(),
            validateOnly=args.validate_only,
            updateMask=','.join(update_mask),
            googleCloudDataplexV1DataScan=datascan.GenerateDatascanForUpdateRequest(
                args
            ),
        )
    )

    if getattr(args, 'validate_only', False):
      log.status.Print('Validation completed. Skipping resource update.')
      return

    async_ = getattr(args, 'async_', False)
    if not async_:
      response = datascan.WaitForOperation(update_req_op)
      log.UpdatedResource(
          response.name,
          details=(
              'Data quality scan updated in project [{0}] with location [{1}]'
              .format(datascan_ref.projectsId, datascan_ref.locationsId)
          ),
      )
      return response

    log.status.Print(
        'Updating data quality scan with path [{0}] and operation [{1}].'
        .format(datascan_ref, update_req_op.name)
    )
    return update_req_op
