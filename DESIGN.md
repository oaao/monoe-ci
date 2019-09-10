# monoe-ci - design

To implement a 'monoecious' CI system:

## components

A **monitor** object, which performs the following actions:

```
- periodically poll the repository to check for change (i.e. a new commit)
    - find current known commit ID
    - update the repository
    - compare current known commit ID with latest commit ID
- notify dispatcher component upon observing change, and provide dispatcher with the newest commit ID
```

A **dispatcher** object, which performs the following actions:

```
- listen for external requests from both monitors and test runners
- allow test runners to 'register' themselves
- given a commit ID from a monitor subprocess, dispatch a test runner against that new commit
- reassign the given commit ID to a new test runner if a previous runner crashed etc.
