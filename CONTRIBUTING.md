# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Workflow

Our project follows the [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow) workflow.  GitHub flow is a branch-based workflow.  The main steps in GitHub flow include:

- Create a branch
- Make changes
- Create a pull request
- Address review comments
- Merge your pull request
- Delete your branch

## How to Contribute

Contributing to `CoordGeomPy` follows the 5 step process outlined below:

1. If you are a first-time contributor:

- Go to https://github.com/UBC-MDS/CoordGeomPy and click the “fork” button to create your own copy of the project.

Clone the project to your local computer:

```{bash}
git clone https://github.com/your-username/CoordGeomPy.git
```

- Change the directory:

```{bash}
cd CoordGeomPy
```

Add the upstream repository:

```{bash}
git remote add upstream https://github.com/UBC-MDS/CoordGeomPy
```

- Now, `git remote -v` will show two remote repositories named:

- `upstream`, which refers to the `CoordGeomPy` repository
- `origin`, which refers to your personal fork

2. Develop your contribution:

- Pull the latest changes from upstream:

```{bash}
git checkout main
git pull upstream main
```

- Create a branch for the feature you want to work on. Since the branch name will appear in the merge message, use a sensible name such as ‘feature-X’ where "X" is the name of the feature you are proposing:

```{bash}
git checkout -b feature-X
```

- Commit locally as you progress (git add and git commit) Use a properly formatted commit message, write tests that fail before your change and pass afterward, run all the tests locally. Be sure to document any changed behavior in docstrings.  We follow the NumPy docstring standard.

3. To submit your contribution

- Push your changes back to your fork on GitHub:

```{bash}
git push origin feature-X
```

- Enter your GitHub username and password (repeat contributors or advanced users can remove this step by connecting to GitHub with SSH).
- Go to GitHub. The new branch will show up with a green Pull Request button. Make sure the title and message are clear, concise, and self- explanatory. Then click the button to submit it.
- If your commit introduces a new feature or changes functionality, post on the mailing list to explain your changes. For bug fixes, documentation updates, etc., this is generally not necessary, though if you do not get any reaction, do feel free to ask for review.

4. Review process:

- If needed, reviewers will write inline and/or general comments on your Pull Request (PR) to help you improve its implementation, documentation and style.
- To update your PR, make your changes on your local repository, commit, run tests, and only if they succeed push to your fork. As soon as those changes are pushed up (to the same branch as before) the PR will update automatically.
- A PR must be approved by at least one core team member (Jordan, Arlin, Nico or Zheren) before merging. Approval means the core team member has carefully reviewed the changes, and the PR is ready for merging.

Note: This contribution workflow is inspired by [NumPy](https://numpy.org/devdocs/dev/index.html).

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any part of the documentation, such as the official docs, docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `CoordGeomPy` project is released with a [Code of Conduct](https://github.com/UBC-MDS/CoordGeomPy/blob/main/CONDUCT.md). By contributing to this project you agree to abide by its terms.
