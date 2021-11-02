Dagster in docker how-to docs
=== 

Requirements
---

- Install [Docker](https://docs.docker.com/get-docker/) on your computer.

Start the system
---

```bash
docker compose up --build
```

This will pull all the important docker images from docker hub and build the infrastructure. After that you will need to go inside the docker container and start the dagster daemon, so the scheduler and the sensors can work! 

```bash
docker exec -it docker_container bash
```

Then run the following command to start the daemons!

```bash
dagster-daemon run
```

If everything is up and running the go to [http://localhost:9000/](http://localhost:9000/), you can find the Dagster UI there. 

There are two pipelines defined in the system, the **etl_pipeline** is responsible for loading data to a postgreDB table. If you turn on the schedule in the UI, then it will run every minute. You can find the source code in the *tutorial.py* file.

The second pipeline is tied to a sensor, which means it will only run if a criteria is met (defined in the sensor). It reads the data from the postgre table and loads it to an other table and also does a bit of transformation on the data. Turn on the sensor so you can try it out and play with it.

If you would like to check the PostgreDB to see if the pipelines are working correctly, then you can connect to it at **localhost:5432**.



