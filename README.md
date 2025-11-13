# STUMPY Automation Bot

# Generating a Personal Access Token (PAT)

In the upper right profile:

1. Click on the profile picture
2. Click on Settings (note that this is **not** the repository settings!)
3. Click on < >  Developer settings located at the bottom of the left hand side menu
4. Click on Personal access tokens > Tokens (classic)
5. Click on Generate new token > Generate new token (classic)
6. Provide a description for the Note and check `public_repo` (without this checked, you will likely receive a 404 error when trying to access the Github API)
7. Click Generate token at the bottom of the page
8. Copy the PAT and store them in a specific environment and secret for future use

# Storing and Using Secrets

In your repository of interest:

1. Click on Settings (note that this is **not** the profile settings)
2. Click on Environments on the left hand side menu
3. Click New environment
4. Add an appropriate environment name like `API_Access`
5. Near the bottom, click Add secret
6. Specify an environment variable name as `ACCESS_TOKEN` and paste your PAT from 
7. Access this environment in your workfow via `environment: API_Access` and reference the secret via `${{ secrets.ACCESS_TOKEN }}`

# Allow Manual Workflow Triggering

In the workflow, add:

```
on:
  workflow_dispatch:
```

This will allow you to manually trigger the workflow within the Actions tab of Github

# Schedule Cron Job within Github Actions

In the workflow, add:

```
on:
  # workflow_dispatch:
  schedule:
    - cron: '0 14 * * *'  # 2pm UTC == 9am EST
```

~~
# Triggering the Workflow Externally Via Github API

In the workflow, specify the `event_type` through the `repository_dispatch` custom event trigger:

```
on:
  # workflow_dispatch:
  # schedule:
  #   - cron: '0 14 * * *'  # 2pm UTC == 9am EST
  repository_dispatch:
    types: [check_numba_python_comptability]
```

Then, this can be triggered through the Github API via cron-job.org:

1. Login to cron-job.org
2. Create a new cron job
3. Choose an appropirate title
4. Set the dispatch URL (e.g., `https://api.github.com/repos/stumpy-dev/automate/dispatches`)
5. Select an execution schedule
6. Click on the "Advanced" tab
7. Add a `Accept:application/vnd.github.v3+json` key-value header 
8. Add a `Authorization:token <Personal_Access_Token>` key-value header 
9. Change the "Request Method" to "POST"
10. And add a `{"event_type": "check_numba_python_compatibility"}` Request body
~~