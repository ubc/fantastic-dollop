FROM "node:10-alpine"

# bash - required to run entrypoint
RUN apk add --no-cache bash

WORKDIR /home/node/app

# hack to run yarn install on container startup, otherwise, you'd
# have to run it manually before you can run the container
COPY docker/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
