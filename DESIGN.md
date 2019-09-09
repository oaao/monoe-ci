# monoe-ci - design

To implement a 'monoecious' CI system:

## component

A **monitor** object, which performs the following actions:

```
- periodically poll the repository to check for change (i.e. a new commit)
    - find current known commit ID
    - update the repository
    - compare current known commit ID with latest commit ID
- notify dispatcher component upon observing change, and provide dispatcher with the newest commit ID
```

