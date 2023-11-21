from github import Github
from github import InputGitTreeElement


github_token = "PUT YOUR TOKEN HERE"
repo_owner = "PUT YOUR USERNAME HERE"
repo_name = "PUT YOUR REPOSITORY NAME HERE"
branch_name = "PUR YOUR BRANCH NAME HERE"


def make_commit(file_path, new_content, commit_message):
    g = Github(github_token)
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    repo_branch = repo.get_branch(branch_name)
    commit = repo_branch.commit
    new_blob = repo.create_git_blob(new_content, "utf-8")
    tree = repo.get_git_tree(commit.sha)
    new_tree = repo.create_git_tree(
        [
            InputGitTreeElement(
                path=file_path,
                mode='100644',
                type='blob',
                sha=new_blob.sha
            )
        ],
        base_tree=tree
    )
    new_commit = repo.create_git_commit(
        message=commit_message,
        tree=repo.get_git_tree(sha=new_tree.sha),
        parents=[repo.get_git_commit(repo.get_branch(branch_name).commit.sha)]
    )
    ref = repo.get_git_ref(ref="heads/main")
    ref.edit(sha=new_commit.sha)
