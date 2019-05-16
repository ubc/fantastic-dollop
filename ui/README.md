# Web Component UI

The frontend.

## Frameworks

* [Vue.js](https://vuejs.org/), JavaScript framework

## Setup (Non-Docker)

#### Prerequisite

* [Yarn](https://yarnpkg.com/en/), JavaScript dependency manager.

#### Install Dependencies

For first time setups or if new dependencies were added, run:

    yarn install

###### Add New Dependencies

If you need to add a new dependency, run:

    yarn add <DEPENDENCY NAME>

`<DEPENDENCY NAME>` is the npm package you want to install.

The server will need to be restarted to load in the new dependencies.

###### Upgrade Dependencies

If you need to upgrade a dependency, run:

    yarn upgrade <DEPENDENCY NAME>

`<DEPENDENCY NAME>` is the npm package you want to install. You can also just run `yarn upgrade` to upgrade everything.

#### Configuration

The API url is configured using environment variable files, documented [here](https://cli.vuejs.org/guide/mode-and-env.html). The included `.env.development` file is configured for the Docker build, so you will have to modify it to your API server's location.

#### Run

This will run locally with dynamic reload, changing the source should automatically reload the page:

    yarn run serve

The site should be available at [http://localhost:8080/](http://localhost:8080/), unless port 8080 is already taken, in which case, it increments the port number until a free one is found.

###### Live Reload Limitations

In practice, I've found that some CSS changes aren't properly processed and you have to do a manual page refresh to properly see the changes. So if you find adding in a class doesn't do what you expected, refresh the page just to be sure.

Environment variable file changes, such as to `.env`, requires an application restart to take effect.

###### Other Commands

* Compiles and minifies for production

        yarn run build

* Run your tests

        yarn run test

* Lints and fixes files

        yarn run lint

#### Vue Customization
See [Configuration Reference](https://cli.vuejs.org/config/).

#### Issues

* When installing packages in the UI using npm or yarn, installation fails with file permission errors.
  This is caused by the docker container mounting the directory and creating files using root permission. You just need to change the owner of the file back to you, e.g.: `sudo chown -R <username> node_modules/`
