---
title: "DLT-META CLI"
date: 2021-08-04T14:25:26-04:00
weight: 7
draft: false
---

### pre-requisites:
- [Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/tutorial.html)
- Once you install Databricks CLI, authenticate your current machine to a Databricks Workspace:
   
   ```commandline
   databricks auth login --host WORKSPACE_HOST
   ```
- Python 3.8.0 +
##### Steps:
1. ``` git clone https://github.com/databrickslabs/dlt-meta.git ```
2. ``` cd dlt-meta ```
3. ``` python -m venv .venv ```
4. ```source .venv/bin/activate ```
5. ``` pip install databricks-sdk ```

![onboardingDLTMeta.gif](/images/onboardingDLTMeta.gif)

## OnboardJob 
### Run Onboarding using dlt-meta cli command: 
 ```shell 
    databricks labs dlt-meta onboard
``` 
-  Above command will prompt you to provide onboarding details.
- If you have cloned dlt-meta git repo then accepting defaults will launch config from [demo/conf](https://github.com/databrickslabs/dlt-meta/tree/main/demo/conf) folder.
- You can create onboarding files e.g onboarding.json, data quality and silver transformations and put it in conf folder as show in [demo/conf](https://github.com/databrickslabs/dlt-meta/tree/main/demo/conf)

![onboardingDLTMeta_2.gif](/images/onboardingDLTMeta_2.gif)

![onboardingDLTMeta.gif](/images/onboardingDLTMeta.gif)

- Once onboarding jobs is finished deploy `bronze` and `silver` DLT using below command

## Dataflow DLT Pipeline: 

#### Deploy Bronze DLT
 ```shell 
        databricks labs dlt-meta deploy
   ```
- Above command will prompt you to provide dlt details. Please provide respective details for schema which you provided in above steps

![deployingDLTMeta_bronze.gif](/images/deployingDLTMeta_bronze.gif)

#### Deploy Silver DLT
 ```shell 
        databricks labs dlt-meta deploy
```
- - Above command will prompt you to provide dlt details. Please provide respective details for schema which you provided in above steps

![deployingDLTMeta_silver.gif](/images/deployingDLTMeta_silver.gif)

- Goto your databricks workspace and located onboarding job under: Workflow->Jobs runs
