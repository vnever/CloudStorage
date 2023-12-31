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
"""'vmware nodes list command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.vmware.nodes import NodesClient
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.vmware import flags

DETAILED_HELP = {
    'DESCRIPTION': """
        List nodes in a VMware Engine private cloud's cluster.
        """,
    'EXAMPLES': """
        To list nodes in the `my-private-cloud` private cloud and `my-cluster` cluster:

          $ {command} --location=us-west2-a --project=my-project --private-cloud=my-private-cloud --cluster=my-cluster

          Or:

          $ {command} --private-cloud=my-private-cloud --cluster=my-cluster

        In the second example, the project and location are taken from gcloud properties core/project and compute/zone.
  """,
}


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.GA)
class List(base.ListCommand):
  """List nodes in a Google Cloud VMware Engine private cloud's cluster."""

  detailed_help = DETAILED_HELP

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    flags.AddClusterArgToParser(parser)
    parser.display_info.AddFormat(
        'table(name.segment(-1):label=NAME,'
        'name.segment(-7):label=LOCATION,'
        'name.segment(-5):label=PRIVATE_CLOUD,'
        'name.segment(-3):label=CLUSTER,'
        'state,nodeTypeId,fqdn,'
        'internalIp)'
    )

  def Run(self, args):
    cluster = args.CONCEPTS.cluster.Parse()
    client = NodesClient()
    return client.List(cluster)
