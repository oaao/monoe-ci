# monoe-ci

A basic continuous integration system written in Python from reference examples.

(currently, it's horrible)


## introduction

`monoe-ci` bases on the loose analogy of a monoecious flower. [ --> [design](./DESIGN.md) ]

It implements a repository `monitor`, a task `dispatcher`, and a `test runner`; however, they each run as independent processes and communicate through sockets (to better manage load, and to be fault-tolerant).

Each component process should on its own networked machine. For a CI system, [monoecy](https://vimeo.com/219945413) is a useful design metaphor but totally counterproductive to literalize into its deployment and usage.


## current limitations

* acts on `git` repositories only

* test discovery is arbitrarily limited to tests that exist in `{repository}/tests/`

* tests run against the latest new commit only, not each new commit since last known

* an observer model & local repos will be used instead of post-commit external hooks and remote repos

* instead of a `reporter` component, results will be dumped to a file local to the `dispatcher` process


## references

* Brown & Canino-Koning (May 2012): [Continuous Integration](https://www.aosabook.org/en/integration.html). *The Architecture of Open Source Applications, Vol. 1*

* Malini Das (Sept 2012): [A Continuous Integration System](http://aosabook.org/en/500L/a-continuous-integration-system.html)