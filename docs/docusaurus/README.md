---
title: Documentation Site
slug: /readme
---

This documentation site is built using [Docusaurus 2](https://v2.docusaurus.io/), a modern static website generator.

## System Requirements

https://docusaurus.io/docs/installation#requirements

## Installation

From the repo root run:

```console
yarn install
```

## Local Development

For the fastest iterative dev loop, start a local server and open up the compiled site in a browser window. Most changes are reflected live without needing server restarts.

```console
yarn start
```

## Linting

[standard.js](https://standardjs.com/) is used to lint the project. Please run the linter before committing changes.

```console
yarn lint
```

## Build

To build a static version of the site, this command generates static content into the `build` directory. This can be served using any static hosting service.

```console
yarn build
```

## Deployment

```console
GIT_USER=<Your GitHub username> USE_SSH=true yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

## Other relevant files

The following are a few details about other files Docusaurus uses that you may wish to be familiar with.

- `../sidebars.js`: JavaScript that specifies the sidebar/navigation used in docs pages
- `../src`: non-docs pages live here
- `../static`: static assets used in docs pages (such as CSS) live here
- `../docusaurus.config.js`: the configuration file for Docusaurus
- `../babel.config.js`: Babel config file used when building
- `../package.json`: dependencies and scripts
- `../yarn.lock`: dependency lock file that ensures reproducibility

sitemap.xml is not in the repo since it is built and uploaded by a netlify plugin during the documentation build process. 

## Documentation changes checklist

1. For any pages you have moved or removed, update _redirects to point from the old to the new content location


## Versioning

To add a new version, follow these steps:

1. Check out the version from the tag, e.g. `git checkout 0.15.50`
2. Run `yarn install`
3. Run `yarn build`
4. Create the version e.g. `yarn docusaurus docs:version 0.15.50`
5. Pull down the version file (see `docs/build_docs` for the file, currently https://superconductive-public.s3.us-east-2.amazonaws.com/oss_docs_versions.zip)
6. Unzip and add your newly created versioned docs via the following:
7. Copy the version you built in step 4 from inside `versioned_docs` in your repo to the `versioned_docs` from the unzipped version file.
8. Copy the version you built in step 4 from inside `versioned_sidebars` in your repo to the `versioned_sidebars` from the unzipped version file.
9. Add your version number to `versions.json` in the unzipped version file.
10. Zip up `versioned_docs`, `versioned_sidebars` and `versions.json` and upload to the s3 bucket (see `docs/build_docs` for the bucket name)
11. Once the docs are built again, this zip file will be used for the versions.