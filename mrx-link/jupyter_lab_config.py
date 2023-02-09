#  MAKINAROCKS CONFIDENTIAL
#  ________________________
#
#  [2017] - [2023] MakinaRocks Co., Ltd.
#  All Rights Reserved.
#
#  NOTICE:  All information contained herein is, and remains
#  the property of MakinaRocks Co., Ltd. and its suppliers, if any.
#  The intellectual and technical concepts contained herein are
#  proprietary to MakinaRocks Co., Ltd. and its suppliers and may be
#  covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law. Dissemination
#  of this information or reproduction of this material is
#  strictly forbidden unless prior written permission is obtained
#  from MakinaRocks Co., Ltd.
#
# pylint: disable=undefined-variable
# flake8: noqa=F821
# type: ignore
# Configuration file for lab.
import os

# ------------------------------------------------------------------------------
# ServerApp(JupyterApp) configuration
# ------------------------------------------------------------------------------
## Set the Access-Control-Allow-Origin header
#
#          Use '*' to allow any origin to access your server.
#
#          Takes precedence over allow_origin_pat.
#  Default: ''
c.ServerApp.allow_origin = "*"

## Whether to allow the user to run the server as root.
#  Default: False
c.ServerApp.allow_root = True

## The base URL for the Jupyter server.
#
#                         Leading and trailing slashes can be omitted,
#                         and will automatically be added.
#  Default: '/'
c.ServerApp.base_url = os.environ.get("NB_PREFIX", "/")

## Disable cross-site-request-forgery protection
#
#          Jupyter notebook 4.3.1 introduces protection from cross-site request forgeries,
#          requiring API requests to either:
#
#          - originate from pages served by this server (validated with XSRF cookie and token), or
#          - authenticate with a token
#
#          Some anonymous compute resources still desire the ability to run code,
#          completely without authentication.
#          These services can disable all authentication and security checks,
#          with the full knowledge of what that implies.
#  Default: False
c.ServerApp.disable_check_xsrf = True


## The IP address the Jupyter server will listen on.
#  Default: 'localhost'
c.ServerApp.ip = "0.0.0.0"

## Whether to open in a browser after starting.
#                          The specific browser used is platform dependent and
#                          determined by the python standard library `webbrowser`
#                          module, unless it is overridden using the --browser
#                          (ServerApp.browser) configuration option.
#  Default: False
c.ServerApp.open_browser = False

## Hashed password to use for web authentication.
#
#                        To generate, type in a python/IPython shell:
#
#                          from jupyter_server.auth import passwd; passwd()
#
#                        The string should be of the form type:salt:hashed-
#  password.
#  Default: ''
c.ServerApp.password = ""

## The port the server will listen on (env: JUPYTER_PORT).
#  Default: 0
c.ServerApp.port = 8888

## The directory to use for notebooks and kernels.
#  Default: ''
c.ServerApp.root_dir = os.path.join(os.environ.get("HOME"), "workspace")

## Token used for authenticating first-time connections to the server.
#
#          The token can be read from the file referenced by JUPYTER_TOKEN_FILE or set directly
#          with the JUPYTER_TOKEN environment variable.
#
#          When no password is enabled,
#          the default is to generate a new, random token.
#
#          Setting to an empty string disables authentication altogether, which
#  is NOT RECOMMENDED.
#  Default: '<generated>'
c.ServerApp.token = ""
