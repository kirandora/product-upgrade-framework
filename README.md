# product-upgrade-framework
Basic framework to upgrade any product
There can be two modes of upgrade support for the product. Online upgrade and offline upgrade.

# Online upgrade flow(Customer connected to internet)
Stage of Upgrade:
1. Download Stage
    1.1 Download the priority apps and upgrade.
    1.2 Download the rest of apps package for upgrade
2. Extract Stage
   2.1 Extract the package to the host machine.
   2.2 Load the docker images and push to local docker registry.
   2.3 In case of a multi node setup pull the docker images from local docker registry to other nodes. 
3. Upgarde stage
   3.1 Perform pre upgrade health check for upgrade compatibility
   3.2 Perform host upgrade, infra upgrade and apps upgrade in sequence.
   3.3 For performance optimization in a multi node setup host upgrade can be run parallely.

# offline upgrade flow(Customers not connected to internet)
Stage of Upgrade:
1. Download stage:
   1.1 Sign file download: Sign file to check the integrity of apps package file(Checksum verification)
   1.2 Package file download: Download the package file(A tar file consisting of all the docker images)
2. Package verification Stage: Validates the package file against the sign file
3. Extract stage:
   2.1 Extract the package to the host machine.
   2.2 Load the docker images and push to local docker registry.
   2.3 In case of a multi node setup pull the docker images from local docker registry to other nodes.
4. Upgarde stage
   4.1 Perform pre upgrade health check for upgrade compatibility
   4.2 Perform host upgrade, infra upgrade and apps upgrade in sequence.
   4.3 For performance optimization in a multi node setup host upgrade can be run parallely.
