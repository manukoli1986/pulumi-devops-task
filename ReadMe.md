# How to Run

install docker on your machine: [Install Docker](https://docs.docker.com/engine/install/)


Open terminal and run:
```
docker-compose up
```

Open a web browser and navigate to 
```
http://localhost:3000
```


# Application Details

- Web: ASP.NET Core 5.0 Web APP
  - this application requires an environment variabled called "ApiAddress" which will be the address of the Web Api.
- API: ASP.NET Core 5.0 Web API

# Solution

[Installing Pulumi](https://www.pulumi.com/docs/get-started/install) and common commands

- pulumi new: creates a new project using a template
- pulumi stack: manage your stacks (at least one is required to perform an update)
- pulumi config: configure variables such as keys, regions, and so on
- pulumi up: preview and deploy changes to your program and/or infrastructure
- pulumi preview: preview your changes explicitly before deploying
- pulumi destroy: destroy your program and its infrastructure when you’re done

### Setup Pulumi to communicate with AWS 
[https://www.pulumi.com/registry/packages/aws/installation-configuration/] (Link)

### 