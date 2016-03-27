# gitlab-webhook-server

Simple argument driven gitlab webhook server.

# About

This small Python script will listen on a given port (--port PORT) for webhook requests
from a given repository (--repo URL), branch (--branch BRANCH) and of a desired type 
(--kind KIND).

When it receives sucn a request it will execute a desired command or script (--post CMD).

# Running

You can start a webhook process like this:

    $ ./gitlab-webhook-server.py --port 5000 \
          --repo ssh://git@gitlab.local/dan/test.git \
          --branch staging \
          --kind push \
          --post /path/to/deploy-to-staging.sh
