# Contributing Guide

Collaborative software development can be intimidating for those who are not used to it -
the code base is often unfamiliar, the tools and conventions novel, 
and the responsibility of writing code that other people will read can feel heavy.
Remember, though, that well-maintained projects, whether individual or collaborative, 
will have similar considerations.
Much of the difficulty in beginning to collaborate is in learning good coding practices.

This document, and the workshop it accompanies, 
should equip you with the knowledge and confidence to start collaborating on software development projects. 
While not every project you work on will have the features referred to,
it's good to have an idea of the kinds of tools available.

## New contributor guide

### Read the README first

When you come to a new project, your first recourse will be the [README](README.md) file. 
This file is so ubiquitous that GitHub automatically displays it below the file list for any directory that has one.
A good README should have an obvious name and be in a human-readable format.
`README` is traditional for plain text files, while this repository has a `README.md` written in markdown.

The README file should give an overview of the project from a user's perspective,
and include instructions for setting up a development version of the project.
Many README files on GitHub include badges that give information about the status of the current code.
These badges can give you a quick indication of the automatic processes in place for analysing contributions.

### Track changes conceptually with Issues

Most software projects have some means of tracking bugs, feature requests, etc.
The Issues tab on the repository hosts GitHub's answer to this challenge.
As with many GitHub features, Issues can be automated extensively, 
but by default they have a brief title, space for a description of the issue, 
and various tags and labels that can be used for categorising and assigning issues to developers. 

In the workshop, we will create an Issue on a repository, write code to fix it, 
and submit a pull request that will automatically close the issue when merged.

### Forks and write access

Provided you can view a repository, you can edit the code. 
_Contributors_ (also called _Maintainers_) can edit the code directly 
(i.e. they can _push_ directly to the remote repository).
You can think of them as having write access to the repository.
Everyone else must create their own copy of the code before they can edit it. 
They do this by _forking_ the repository (usually - you can also just download the code directly).
A fork is a copy of the repository owned by whoever forked it. 
You can think of it as a _branch_ with a different owner.

### Set up a local development version

Most repositories will have instructions on how to get the local development version of your repository up and running
in the README file. You should be a collaborator on the project (ask if you're not), so clone the repository 
and follow the setup instructions.

### Create a branch

Your changes should be kept isolated from everyone else's changes.
The easiest way to do this is by creating your own _branch_ and making the changes there.
Create a branch called `unit/unitname` (e.g. `unit/yard`) for the unit you created in your issue above.

### Write a new unit

Open up the project in your editor of choice, and make sure you understand how the code fits together.
Once you've done that, you can make a new unit in `./src/oxrse_unit_conv/units.py`. 
If your new unit is not an SI unit, and its SI unit is not in `./src/oxrse_unit_conv/si.py` you will need to 
create its corresponding SI unit, too.
Commit the code to your new branch, and push the branch to the remote repository.

### Pull Request

When you're finished with the changes, create a _pull request_, also known as a _PR_.
A pull request 'pulls' commits from one branch into another.
We want to create a pull request from your branch to `main`.
- If you run into any merge issues, checkout this [git tutorial](https://github.com/skills/resolve-merge-conflicts) 
  to help you resolve merge conflicts and other issues.
