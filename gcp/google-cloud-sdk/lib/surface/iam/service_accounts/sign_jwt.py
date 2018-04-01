# Copyright 2017 Google Inc. All Rights Reserved.
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
"""Command for signing jwts for service accounts."""

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iam import base_classes
from googlecloudsdk.command_lib.iam import iam_util
from googlecloudsdk.core import log


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class SignJwt(base_classes.BaseIamCommand):
  """Sign a JWT with a managed service account key.

  This command signs a JWT using a system-managed service account key.

  ## EXAMPLES:
  To create a sign JWT with a system-managed service account key,
  run:

    $ {command} --iam-account my-account@somedomain.com input.json output.jwt

  ## SEE ALSO:
  For more information on how this command ties into the wider cloud
  infrastructure, please see
  [](https://cloud.google.com/appengine/docs/java/appidentity/).
  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        '--iam-account', required=True, help='The service account to sign as.')

    parser.add_argument(
        'input',
        metavar='INPUT-FILE',
        help='A path to the file containing the JSON'
        ' JWT Claim set to be signed.')

    parser.add_argument(
        'output',
        metavar='OUTPUT-FILE',
        help='A path the resulting signed JWT will be '
        'written to.')

  def Run(self, args):
    response = self.iam_client.projects_serviceAccounts.SignJwt(
        self.messages.IamProjectsServiceAccountsSignJwtRequest(
            name=iam_util.EmailToAccountResourceName(args.iam_account),
            signJwtRequest=self.messages.SignJwtRequest(payload=self.ReadFile(
                args.input))))

    log.WriteToFileOrStdout(
        args.output, content=response.signedJwt, binary=True)
    log.status.Print(
        'signed jwt [{0}] as [{1}] for [{2}] using key [{3}]'.format(
            args.input, args.output, args.iam_account, response.keyId))
