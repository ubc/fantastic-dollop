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

#### Run

This will run locally with dynamic reload, changing the source should automatically reload the page:

    yarn run serve

In practice though, I've found that some CSS changes aren't properly processed and you have to do a manual page refresh to properly see the changes.

The site should be available at [http://localhost:8080/](http://localhost:8080/), unless port 8080 is already taken, in which case, it increments the port number until a free one is found.

###### Other Commands

* Compiles and minifies for production

        yarn run build

* Run your tests

        yarn run test

* Lints and fixes files

        yarn run lint

#### Vue Customization
See [Configuration Reference](https://cli.vuejs.org/config/).
