# Commands used at work

## Initialize a new Git repository
```git 
git init
```
## Check the status of the working directory
```git 
git status
```
## Stage all changes for commit
```git 
git add .
```
## Create a new branch
```git 
git branch [name_branch]
```
## Rename the current branch from main to master
```git 
git branch -m main master
```
## Commit changes with a message
```git 
git commit -m "[name_branch] message"
```
## Push the branch to the remote repository and set upstream tracking
```git 
git push -u origin [name_branch]
```
## Merge a branch into the current branch with a merge commit (no fast-forward)
```git 
git merge --no--ff [name_branch]
```
## Create a new tag
```git 
git tag [name_tag]
```
## Push a tag to the remote repository
```git 
git push origin [name_tag]
```
## Switch to a specific branch
```git 
git checkout [name_branch]
```
## View commit history
```git 
git log
```
## Apply a specific commit to the current branch
```git 
git cherry-pick [commit_hash]
```
## List or create tags
```git 
git tag
```
## List branches
```git 
git branch 
```
## Delete a branch (only if it has been merged)
```git 
git branch -d [name_branch]
```
